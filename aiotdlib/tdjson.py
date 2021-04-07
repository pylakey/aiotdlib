import json
import logging
import platform
import typing
from ctypes import *
from enum import IntEnum

import pkg_resources

fatal_error_callback_type = CFUNCTYPE(None, c_char_p)

TDLIB_VERSION = '1.7.3'
TDLIB_MAX_INT = 2 ** 63 - 1


def _get_tdjson_lib_path() -> str:
    if platform.system().lower() == 'darwin':
        lib_extension = 'dylib'
    elif platform.system().lower() == 'windows':
        lib_extension = 'dll'
    else:
        lib_extension = 'so'

    lib_name = f"libtdjson.{TDLIB_VERSION}.{lib_extension}"

    return pkg_resources.resource_filename('aiotdlib', f'tdlib/{lib_name}')


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
    __td_json_client_create: typing.Callable[[], int]
    __td_json_client_receive: typing.Callable[[int, float], bytes]
    __td_json_client_send: typing.Callable[[int, bytes], None]
    __td_json_client_execute: typing.Callable[[int, bytes], bytes]
    __td_json_client_destroy: typing.Callable[[int], None]
    __td_set_log_verbosity_level: typing.Callable[[int], None]
    __td_set_log_fatal_error_callback: typing.Callable[[fatal_error_callback_type], None]
    __c_on_fatal_error_callback: typing.Callable[[fatal_error_callback_type], None]

    td_json_client: typing.Optional[int] = None

    def __init__(self, library_path: str = None, verbosity: TDLibLogVerbosity = TDLibLogVerbosity.WARNING) -> None:
        if library_path is None:
            library_path = _get_tdjson_lib_path()

        if library_path is None:
            raise ValueError('Unable to find TD library binaries')

        self.logger = logging.getLogger(__name__)
        self.logger.info('Using shared library "%s"', library_path)
        self.initialize(library_path, verbosity)

    def __del__(self) -> None:
        self.stop()

    def initialize(self, library_path: str, verbosity: TDLibLogVerbosity) -> None:
        if bool(self.td_json_client):
            raise RuntimeError('TDJson instance is already initialized')

        # load TDLib functions from shared library
        self.__tdjson = CDLL(library_path)

        # td_json_client_create
        self.__td_json_client_create = self.__tdjson.td_json_client_create
        self.__td_json_client_create.restype = c_void_p
        self.__td_json_client_create.argtypes = []

        # Creating tdlib json client instance
        self.td_json_client = self.__td_json_client_create()

        # td_json_client_receive
        self.__td_json_client_receive = self.__tdjson.td_json_client_receive
        self.__td_json_client_receive.restype = c_char_p
        self.__td_json_client_receive.argtypes = [c_void_p, c_double]

        # td_json_client_send
        self.__td_json_client_send = self.__tdjson.td_json_client_send
        self.__td_json_client_send.restype = None
        self.__td_json_client_send.argtypes = [c_void_p, c_char_p]

        # td_json_client_execute
        self.__td_json_client_execute = self.__tdjson.td_json_client_execute
        self.__td_json_client_execute.restype = c_char_p
        self.__td_json_client_execute.argtypes = [c_void_p, c_char_p]

        # td_json_client_destroy
        self.__td_json_client_destroy = self.__tdjson.td_json_client_destroy
        self.__td_json_client_destroy.restype = None
        self.__td_json_client_destroy.argtypes = [c_void_p]

        # td_set_log_verbosity_level
        self.__td_set_log_verbosity_level = self.__tdjson.td_set_log_verbosity_level
        self.__td_set_log_verbosity_level.restype = None
        self.__td_set_log_verbosity_level.argtypes = [c_int]
        self.__td_set_log_verbosity_level(int(verbosity))

        # td_set_log_fatal_error_callback
        self.__td_set_log_fatal_error_callback = self.__tdjson.td_set_log_fatal_error_callback
        self.__td_set_log_fatal_error_callback.restype = None
        self.__td_set_log_fatal_error_callback.argtypes = [fatal_error_callback_type]
        c_on_fatal_error_callback = fatal_error_callback_type(self.__on_fatal_error_callback)
        self.__td_set_log_fatal_error_callback(c_on_fatal_error_callback)

    def __on_fatal_error_callback(self, error_message: str) -> None:
        self.logger.error('TDLib fatal error: %s', error_message)

    def send(self, query: dict):
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        # TODO: Add support for orjson for better encoding/decoding performance
        dumped_query = json.dumps(query).encode('utf-8')
        self.logger.debug(f'[me >>>] Sending {dumped_query}')
        self.__td_json_client_send(self.td_json_client, dumped_query)

    def execute(self, query: dict) -> typing.Optional[dict]:
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        # TODO: Add support for orjson for better encoding/decoding performance
        dumped_query = json.dumps(query).encode('utf-8')
        self.logger.debug(f'Executing query {dumped_query} as client {self.td_json_client}')
        result = self.__td_json_client_execute(self.td_json_client, dumped_query)

        if result:
            result = json.loads(result)

        return result

    def receive(self, timeout: float = 1.0) -> typing.Optional[dict]:
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        result = self.__td_json_client_receive(self.td_json_client, timeout)

        if result:
            self.logger.debug(f'[me <<<] Received {result}')
            result = json.loads(result)

        return result

    def stop(self) -> None:
        if bool(self.td_json_client) and callable(self.__td_json_client_destroy):
            self.logger.warning('Destroying TDJson client')
            td_json_client = self.td_json_client
            self.td_json_client = None
            self.__td_json_client_destroy(td_json_client)
