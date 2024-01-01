from __future__ import annotations

import asyncio
import logging
import pathlib
import platform
import sys
import typing
from ctypes import *
from ctypes.util import find_library
from enum import IntEnum

import ujson

from .types import Packet
from .types import Query
from .utils import encode_query

LogMessageCallback = CFUNCTYPE(None, c_int, c_char_p)
ARCH_ALIASES = {
    "x86_64": "amd64",
    "aarch64": "arm64",
    "arm64v8": "arm64",
}
SYSTEM_LIB_EXTENSION = {
    'darwin': 'dylib',
    'linux': 'so',
    'freebsd': 'so',
}


def _get_bundled_tdjson_lib_path() -> str:
    tdjson_path = find_library('tdjson')

    if tdjson_path is not None:
        return tdjson_path

    uname = platform.uname()
    system_name = uname.system.lower()
    machine_name = uname.machine.lower()
    machine_name = ARCH_ALIASES.get(machine_name, machine_name)
    extension = SYSTEM_LIB_EXTENSION.get(system_name)

    if not bool(extension):
        raise RuntimeError('Prebuilt TDLib binary is not included for this system')

    binary_name = f'libtdjson_{system_name}_{machine_name}.{extension}'
    return str((pathlib.Path(__file__) / 'tdlib' / binary_name).absolute())


class TDLibLogVerbosity(IntEnum):
    FATAL = 0
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4
    VERBOSE = 5
    MAXIMUM = 1023


class CoreTDJson:
    def __init__(self, library_path: str | pathlib.Path) -> None:
        self.logger = logging.getLogger(__name__)

        if not bool(library_path):
            raise ValueError('Library path must be provided')

        library_path = pathlib.Path(library_path)

        if not bool(library_path.exists()):
            raise FileNotFoundError('Library path does not exist')

        if not bool(library_path.is_file()):
            raise IsADirectoryError('Library path must point to a binary file')

        self.logger.info('Using "%s" TDLib binary', library_path)

        # TDLib functions typings
        self.__td_send: typing.Callable[[int, bytes], None]
        self.__td_execute: typing.Callable[[bytes], bytes]
        self.__td_set_log_message_callback: typing.Callable[[LogMessageCallback], None]

        # load TDLib functions from shared library
        self.__tdjson: CDLL = CDLL(str(library_path))

        # TDJSON_EXPORT int td_create_client_id();
        self.__td_create_client_id: typing.Callable[[], int] = self.__tdjson.td_create_client_id
        self.__td_create_client_id.restype = c_int
        self.__td_create_client_id.argtypes = []

        # TDJSON_EXPORT const char *td_receive(double timeout);
        self.__td_receive: typing.Callable[[float], bytes] = self.__tdjson.td_receive
        self.__td_receive.restype = c_char_p
        self.__td_receive.argtypes = [c_double]

        # TDJSON_EXPORT void td_send(int client_id, const char *request);
        self.__td_send: typing.Callable[[int, bytes], None] = self.__tdjson.td_send
        self.__td_send.restype = None
        self.__td_send.argtypes = [c_int, c_char_p]

        # TDJSON_EXPORT const char *td_execute(const char *request);
        self.__td_execute: typing.Callable[[bytes], bytes] = self.__tdjson.td_execute
        self.__td_execute.restype = c_char_p
        self.__td_execute.argtypes = [c_char_p]

        # td_set_log_message_callback
        self.__td_set_log_message_callback: typing.Callable[
            [LogMessageCallback],
            None
        ] = self.__tdjson.td_set_log_message_callback
        self.__td_set_log_message_callback.restype = None
        self.__td_set_log_message_callback.argtypes = [LogMessageCallback]
        self.__td_set_log_message_callback(LogMessageCallback(self.__log_message_callback))

    def __log_message_callback(self, verbosity_level: int, message: str) -> None:
        if verbosity_level == TDLibLogVerbosity.FATAL:
            self.logger.error('TDLib FATAL error: %s', message)

        sys.stdout.flush()


class TDJson(CoreTDJson):
    def __init__(
            self,
            library_path: str | pathlib.Path,
            verbosity: TDLibLogVerbosity = TDLibLogVerbosity.ERROR,
            loop: typing.Optional[asyncio.AbstractEventLoop, None] = None
    ) -> None:
        super().__init__(library_path)
        self.__clients = dict[int, TDJsonClient]()
        self.__loop: typing.Optional[asyncio.AbstractEventLoop] = loop
        self.__listen_task: typing.Optional[asyncio.Task] = None
        self.execute({'@type': 'setLogVerbosityLevel', 'new_verbosity_level': verbosity})

    def __del__(self) -> None:
        for client_id in self.__clients:
            self.close_client(client_id)
        self.__listen_task.cancel()

    def send(self, query: Query, client_id: int):
        query = encode_query(query)
        self.logger.debug('[%s >>>] Sending %s', client_id, query)
        self.__td_send(client_id, query)

    def execute(self, query: Query) -> typing.Optional[Packet]:
        query = encode_query(query)
        self.logger.debug('Executing query %s', query)
        result = self.__td_execute(query)

        if result:
            result = ujson.loads(result)

        return result

    def receive(self, timeout: float = 10.0) -> typing.Optional[Packet]:
        result = self.__td_receive(timeout)

        if bool(result):
            result = ujson.loads(result)

        return result

    def close_client(self, client_id: int) -> None:
        # TDLib client instances are destroyed automatically after they are closed, so we need to send close
        self.send({'@type': 'close'}, client_id)

    def subscribe(self, client: TDJsonClient) -> int:
        if self.__loop is None:
            self.__loop = asyncio.get_running_loop()

        if self.__listen_task is None:
            self.logger.debug("Starting listen task")
            self.__listen_task = self.__loop.create_task(self.listen())

        client_id = self.__td_create_client_id()
        self.__clients[client_id] = client
        return client_id

    def unsubscribe(self, client_id: int) -> None:
        self.__clients.pop(client_id, None)

        if len(self.__clients) == 0:
            self.__listen_task.cancel()

    async def listen(self):
        while True:
            packet = await self.__loop.run_in_executor(None, self.receive)

            if not isinstance(packet, Packet):
                continue

            client_id = packet.pop('@client_id', 0)

            if not bool(client_id):
                continue

            self.logger.debug('[%s <<<] Received %s', client_id, packet)
            client = self.__clients.get(client_id)

            if isinstance(client, TDJsonClient):
                await client.enqueue(packet)


DEFAULT_TDJSON = TDJson(library_path=_get_bundled_tdjson_lib_path())


class TDJsonClient:
    @classmethod
    def create(
            cls,
            library_path: typing.Optional[str] = None,
            tdlib_verbosity: TDLibLogVerbosity = TDLibLogVerbosity.ERROR,
    ):
        if not bool(library_path):
            return cls(DEFAULT_TDJSON)

        tdjson = TDJson(library_path=library_path, verbosity=tdlib_verbosity)
        return cls(tdjson)

    def __init__(self, td_json: TDJson):
        super().__init__()
        self.__queue = asyncio.Queue[Packet]()
        self.__loop = asyncio.get_running_loop()
        self.td_json = td_json
        self.client_id = td_json.subscribe(self)
        self.logger = logging.getLogger(f"{self.__class__.__name__}:{self.client_id}")

    async def __run_in_executor(self, func: typing.Callable, *args):
        return await self.__loop.run_in_executor(None, func, *args)

    async def send(self, query: Query) -> None:
        return await self.__run_in_executor(self.td_json.send, query, self.client_id)

    async def execute(self, query: Query) -> typing.Optional[Packet]:
        return await self.__run_in_executor(self.td_json.execute, query)

    async def stop(self) -> None:
        self.td_json.unsubscribe(self.client_id)
        return await self.__run_in_executor(self.td_json.close_client, self.client_id)

    async def receive(self) -> Packet:
        return await self.__queue.get()

    async def enqueue(self, packet: Packet) -> None:
        await self.__queue.put(packet)
