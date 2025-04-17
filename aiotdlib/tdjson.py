from __future__ import annotations

import asyncio
import logging
import pathlib
import platform
import sys
import typing
from ctypes import CDLL, CFUNCTYPE, c_char_p, c_double, c_int
from ctypes.util import find_library
from enum import IntEnum

import ujson

TDJsonQuery = typing.Union[str, bytes, dict]
LogMessageCallback = CFUNCTYPE(None, c_int, c_char_p)
LogMessageCallbackT = typing.Callable[[int, str], None]


ARCH_ALIASES = {
    "x86_64": "amd64",
    "amd64": "amd64",
    "aarch64": "arm64",
    "arm64": "arm64",
    "arm64v8": "arm64",
}
SYSTEM_LIB_EXTENSION = {
    "darwin": "dylib",
    "linux": "so",
    "freebsd": "so",
}

logger = logging.getLogger(__name__)


def _get_bundled_tdjson_lib_path() -> str:
    tdjson_path = find_library("tdjson")

    if tdjson_path is not None:
        return tdjson_path

    uname = platform.uname()
    system_name = uname.system.lower()
    machine_name = uname.machine.lower()
    machine_name = ARCH_ALIASES.get(machine_name, machine_name)
    extension = SYSTEM_LIB_EXTENSION.get(system_name)

    if not bool(extension):
        raise RuntimeError("Prebuilt TDLib binary is not included for this system")

    binary_name = f"libtdjson_{system_name}_{machine_name}.{extension}"
    bundled_lib_path = (pathlib.Path(__file__).parent / "tdlib" / binary_name).resolve()
    logger.info("Current system: %s %s", system_name, machine_name)
    logger.info("Bundled TDLib binary: %s", bundled_lib_path)
    return str(bundled_lib_path)


def _encode_tdjson_query(query: TDJsonQuery) -> bytes:
    if isinstance(query, dict):
        return ujson.dumps(query, ensure_ascii=False).encode("utf-8")
    elif isinstance(query, str):
        return query.encode("utf-8")
    elif isinstance(query, bytes):
        return query

    raise ValueError("Query has wrong type")


class TDLibLogVerbosity(IntEnum):
    FATAL = 0
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4
    VERBOSE = 5
    MAXIMUM = 1023


class CoreTDJson:
    def __init__(self, library_path: str | pathlib.Path):
        self.logger = logging.getLogger(__name__)

        if not bool(library_path):
            raise ValueError("Library path must be provided")

        library_path = pathlib.Path(library_path).resolve()

        if not bool(library_path.exists()):
            raise FileNotFoundError(f"Library path {library_path} does not exist")

        if not bool(library_path.is_file()):
            raise IsADirectoryError(f"Library path {library_path} must point to a binary file")

        self.logger.info('Using "%s" TDLib binary', library_path)
        self.library_path = library_path

        # TDLib functions typings
        # load TDLib functions from shared library
        self._tdjson: CDLL = CDLL(str(self.library_path))

        # TDJSON_EXPORT int td_create_client_id();
        self._td_create_client_id: typing.Callable[[], int] = self._tdjson.td_create_client_id
        self._td_create_client_id.restype = c_int
        self._td_create_client_id.argtypes = []

        # TDJSON_EXPORT const char *td_receive(double timeout);
        self._td_receive: typing.Callable[[float], bytes] = self._tdjson.td_receive
        self._td_receive.restype = c_char_p
        self._td_receive.argtypes = [c_double]

        # TDJSON_EXPORT void td_send(int client_id, const char *request);
        self._td_send: typing.Callable[[int, bytes], None] = self._tdjson.td_send
        self._td_send.restype = None
        self._td_send.argtypes = [c_int, c_char_p]

        # TDJSON_EXPORT const char *td_execute(const char *request);
        self._td_execute: typing.Callable[[bytes], bytes] = self._tdjson.td_execute
        self._td_execute.restype = c_char_p
        self._td_execute.argtypes = [c_char_p]

        # td_set_log_message_callback
        self._td_set_log_message_callback: typing.Callable[[LogMessageCallbackT], None] = (
            self._tdjson.td_set_log_message_callback
        )
        self._td_set_log_message_callback.restype = None
        self._td_set_log_message_callback.argtypes = [LogMessageCallback]
        self._td_set_log_message_callback(LogMessageCallback(self.__log_message_callback))

    def __log_message_callback(self, verbosity_level: int, message: str) -> None:
        if verbosity_level == TDLibLogVerbosity.FATAL:
            self.logger.error("[TDLib FATAL ERROR]: %s", message)
        elif verbosity_level == TDLibLogVerbosity.ERROR:
            self.logger.error("[TDLib ERROR]: %s", message)
        elif verbosity_level == TDLibLogVerbosity.WARNING:
            self.logger.warning("[TDLib WARNING]: %s", message)
        elif verbosity_level == TDLibLogVerbosity.INFO:
            self.logger.info("[TDLib INFO]: %s", message)
        elif verbosity_level == TDLibLogVerbosity.DEBUG:
            self.logger.debug("[TDLib DEBUG]: %s", message)

        sys.stdout.flush()

    def send(self, client_id: int, query: TDJsonQuery):
        query = _encode_tdjson_query(query)
        self.logger.debug("[Client %s >>>] Sending %s", client_id, query)
        self._td_send(client_id, query)

    def execute(self, query: TDJsonQuery) -> typing.Optional[dict]:
        query = _encode_tdjson_query(query)
        self.logger.debug("Executing query %s", query)
        result = self._td_execute(query)

        if result:
            self.logger.debug("Query result: %s", result)
            result = ujson.loads(result)

        return result

    def receive(self, timeout: float = 10.0) -> typing.Optional[dict]:
        result = self._td_receive(timeout)

        if bool(result):
            self.logger.debug("Received %s", result)
            result = ujson.loads(result)

        return result

    def create_client_id(self) -> int:
        client_id = self._td_create_client_id()
        self.logger.debug("Created new client ID: %d", client_id)
        return client_id

    def close_client(self, client_id: int):
        # TDLib client instances are destroyed automatically after they are closed
        self.send(client_id, {"@type": "close"})


class TDJson(CoreTDJson):
    def __init__(self, library_path: str | pathlib.Path):
        super().__init__(library_path)
        self._subscribed_clients: dict[int, TDJsonClient] = {}
        self._listen_task: typing.Optional[asyncio.Task] = None

    def subscribe_updates(self, client_id: int, client: TDJsonClient):
        if self._listen_task is None:
            self._listen_task = asyncio.create_task(self._listen_updates())

        self._subscribed_clients[client_id] = client

    def unsubscribe_updates(self, client_id: int):
        if bool(client_id) and client_id in self._subscribed_clients:
            self._subscribed_clients.pop(client_id, None)

        if len(self._subscribed_clients) == 0 and bool(self._listen_task) and not self._listen_task.cancelled():
            self._listen_task.cancel()

    async def _listen_updates(self):
        try:
            while True:
                update = await asyncio.to_thread(self.receive)

                if update:
                    client_id = update.get("@client_id")

                    if client_id in self._subscribed_clients:
                        await self._subscribed_clients[client_id].enqueue_update(update)
        except (asyncio.CancelledError, KeyboardInterrupt):
            self._subscribed_clients.clear()
            self._listen_task = None
            raise


class TDJsonClient:
    @classmethod
    def create(cls, library_path: typing.Optional[str] = None):
        if bool(library_path):
            td_json = TDJson(library_path=library_path)
        else:
            td_json = TDJson(library_path=_get_bundled_tdjson_lib_path())

        return cls(td_json)

    def __init__(self, td_json: TDJson):
        self.td_json = td_json
        self.client_id: typing.Optional[int] = td_json.create_client_id()
        self.logger = logging.getLogger(f"{self.__class__.__name__}:{self.client_id}")
        self._updates_queue: asyncio.Queue[dict] = asyncio.Queue()

    def _subscribe(self):
        if not self.client_id:
            self.client_id = self.td_json.create_client_id()
            self.logger = logging.getLogger(f"{self.__class__.__name__}:{self.client_id}")

        self.td_json.subscribe_updates(self.client_id, self)

    def _unsubscribe(self):
        if self.client_id:
            self.td_json.unsubscribe_updates(self.client_id)
            self.client_id = None

    def _cleanup(self):
        # Clear the queue in case of cancellation
        while not self._updates_queue.empty():
            self._updates_queue.get_nowait()

    async def send(self, query: TDJsonQuery):
        self._subscribe()
        return await asyncio.to_thread(self.td_json.send, self.client_id, query)

    async def execute(self, query: TDJsonQuery) -> typing.Optional[dict]:
        return await asyncio.to_thread(self.td_json.execute, query)

    async def close(self):
        if not bool(self.client_id):
            return

        await asyncio.to_thread(self.td_json.close_client, self.client_id)
        self._unsubscribe()

    async def receive(self) -> typing.AsyncGenerator[dict, None]:
        while True:
            try:
                message = await self._updates_queue.get()
                yield message
            except (asyncio.CancelledError, KeyboardInterrupt):
                self._cleanup()
                raise

    async def enqueue_update(self, update: dict) -> None:
        await self._updates_queue.put(update)
