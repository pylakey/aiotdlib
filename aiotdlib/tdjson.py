import asyncio
import logging
import platform
import sys
import typing
from ctypes import *
from ctypes.util import find_library
from enum import IntEnum

import pkg_resources
import ujson

from aiotdlib.utils import (
    Query,
    encode_query,
)

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


def _get_tdjson_lib_path() -> str:
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

    binary_path = f'tdlib/libtdjson_{system_name}_{machine_name}.{extension}'

    return pkg_resources.resource_filename('aiotdlib', binary_path)


class TDLibLogVerbosity(IntEnum):
    FATAL = 0
    ERROR = 1
    WARNING = 2
    INFO = 3
    DEBUG = 4
    VERBOSE = 5
    MAXIMUM = 1023


class TDJson:
    logger: logging.Logger

    # TDLib functions typings
    __tdjson: CDLL
    __td_create_client_id: typing.Callable[[], int]
    __td_receive: typing.Callable[[float], bytes]
    __td_send: typing.Callable[[int, bytes], None]
    __td_execute: typing.Callable[[bytes], bytes]
    __td_set_log_message_callback: typing.Callable[[log_message_callback_type], None]

    def __init__(self, library_path: str = None, verbosity: TDLibLogVerbosity = TDLibLogVerbosity.ERROR) -> None:
        if library_path is None:
            library_path = _get_tdjson_lib_path()

        if library_path is None:
            raise ValueError('Unable to find TD library binaries')

        self.logger = logging.getLogger(__name__)
        self.logger.info('Using shared library "%s"', library_path)
        self.initialize(library_path, verbosity)

        self.__clients = dict[int, ClientTDJson]()
        self.__loop: typing.Optional[asyncio.AbstractEventLoop] = None
        self.__listen_task: typing.Optional[asyncio.Task] = None

    def __del__(self) -> None:
        for client_id in self.__clients:
            self.stop(client_id)
        self.__listen_task.cancel()

    def inject_library(self, library_path: str):
        # load TDLib functions from shared library
        self.__tdjson = CDLL(library_path)

        # TDJSON_EXPORT int td_create_client_id();
        self.__td_create_client_id = self.__tdjson.td_create_client_id
        self.__td_create_client_id.restype = c_int
        self.__td_create_client_id.argtypes = []

        # TDJSON_EXPORT const char *td_receive(double timeout);
        self.__td_receive = self.__tdjson.td_receive
        self.__td_receive.restype = c_char_p
        self.__td_receive.argtypes = [c_double]

        # TDJSON_EXPORT void td_send(int client_id, const char *request);
        self.__td_send = self.__tdjson.td_send
        self.__td_send.restype = None
        self.__td_send.argtypes = [c_int, c_char_p]

        # TDJSON_EXPORT const char *td_execute(const char *request);
        self.__td_execute = self.__tdjson.td_execute
        self.__td_execute.restype = c_char_p
        self.__td_execute.argtypes = [c_char_p]

        # td_set_log_message_callback
        self.__td_set_log_message_callback = self.__tdjson.td_set_log_message_callback
        self.__td_set_log_message_callback.restype = None
        self.__td_set_log_message_callback.argtypes = [log_message_callback_type]

    def initialize(self, library_path: str, verbosity: TDLibLogVerbosity) -> None:
        self.inject_library(library_path)

        self.__td_set_log_message_callback(log_message_callback_type(self.__log_message_callback))
        self.execute({'@type': 'setLogVerbosityLevel', 'new_verbosity_level': verbosity})

    def send(self, query: Query, client_id: int):
        query = encode_query(query)
        self.logger.debug('[%s >>>] Sending %s', client_id, query)
        self.__td_send(client_id, query)

    def execute(self, query: Query) -> typing.Optional[dict]:
        query = encode_query(query)
        self.logger.debug('Executing query %s', query)
        result = self.__td_execute(query)

        if result:
            result = ujson.loads(result)

        return result

    def receive(self, timeout: float = 10.0) -> typing.Optional[dict]:
        result = self.__td_receive(timeout)

        if bool(result):
            result = ujson.loads(result)

        return result

    def stop(self, client_id: int) -> None:
        # TDLib client instances are destroyed automatically after they are closed, so we need to send close
        self.send({'@type': 'close'}, client_id)

    def __log_message_callback(self, verbosity_level: int, message: str) -> None:
        if verbosity_level == TDLibLogVerbosity.FATAL:
            self.logger.error('TDLib fatal error: %s', message)

        sys.stdout.flush()

    def new_client(self):
        """
        Instantiate a new client
        """
        if self.__loop is None:
            self.__loop = asyncio.get_running_loop()
        if self.__listen_task is None:
            self.logger.debug("Starting listen task")
            self.__listen_task = self.__loop.create_task(self.listen())
        client_id = self.__td_create_client_id()
        client = self.__clients[client_id] = ClientTDJson(client_id)
        return client

    async def listen(self):
        while True:
            result = await self.__loop.run_in_executor(None, self.receive)
            if result is None:
                continue
            client_id = result.pop('@client_id', None)
            self.logger.debug('[%s <<<] Received %s', client_id, result)
            if client_id is None:
                continue
            await self.__clients[client_id].queue.put(result)


class ClientTDJson:
    """
    Must not be instantiated directly but rather through the new_client()
    function
    """

    def __init__(self, client_id: int):
        self.client_id = client_id
        self.__loop = asyncio.get_running_loop()
        self.queue = asyncio.Queue[dict]()
        self.logger = logging.getLogger(f"{self.__class__.__name__}:{self.client_id}")

    async def __run_in_executor(self, func: typing.Callable, *args):
        return await self.__loop.run_in_executor(None, func, *args)

    async def send(self, query: Query) -> None:
        return await self.__run_in_executor(td_json.send, query, self.client_id)

    async def receive(self) -> dict:
        return await self.queue.get()

    async def execute(self, query: Query) -> typing.Optional[dict]:
        return await self.__run_in_executor(td_json.execute, query)

    async def stop(self) -> None:
        return await self.__run_in_executor(td_json.stop, self.client_id)


td_json = TDJson()


def create_client() -> ClientTDJson:
    return td_json.new_client()
