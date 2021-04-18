import logging
import platform
import typing
from ctypes import *
from enum import IntEnum

import pkg_resources
import ujson

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
    __td_json_client_receive: typing.Callable[[float], bytes]
    __td_json_client_send: typing.Callable[[int, bytes], None]
    __td_json_client_execute: typing.Callable[[bytes], bytes]
    __td_set_log_verbosity_level: typing.Callable[[int], None]
    __td_set_log_fatal_error_callback: typing.Callable[[fatal_error_callback_type], None]

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

    def inject_library(self, library_path: str):
        # load TDLib functions from shared library
        self.__tdjson = CDLL(library_path)

        # TDJSON_EXPORT int td_create_client_id();
        self.__td_json_client_create = self.__tdjson.td_create_client_id
        self.__td_json_client_create.restype = c_int
        self.__td_json_client_create.argtypes = []

        # TDJSON_EXPORT void td_send(int client_id, const char *request);
        self.__td_json_client_send = self.__tdjson.td_send
        self.__td_json_client_send.restype = None
        self.__td_json_client_send.argtypes = [c_int, c_char_p]

        # TDJSON_EXPORT const char *td_receive(double timeout);
        self.__td_json_client_receive = self.__tdjson.td_receive
        self.__td_json_client_receive.restype = c_char_p
        self.__td_json_client_receive.argtypes = [c_double]

        # TDJSON_EXPORT const char *td_execute(const char *request);
        self.__td_json_client_execute = self.__tdjson.td_execute
        self.__td_json_client_execute.restype = c_char_p
        self.__td_json_client_execute.argtypes = [c_char_p]

        # td_set_log_verbosity_level
        self.__td_set_log_verbosity_level = self.__tdjson.td_set_log_verbosity_level
        self.__td_set_log_verbosity_level.restype = None
        self.__td_set_log_verbosity_level.argtypes = [c_int]

        # td_set_log_fatal_error_callback
        self.__td_set_log_fatal_error_callback = self.__tdjson.td_set_log_fatal_error_callback
        self.__td_set_log_fatal_error_callback.restype = None
        self.__td_set_log_fatal_error_callback.argtypes = [fatal_error_callback_type]

    def initialize(self, library_path: str, verbosity: TDLibLogVerbosity) -> None:
        self.inject_library(library_path)

        if bool(self.td_json_client):
            raise RuntimeError('TDJson instance is already initialized')

        self.__td_set_log_fatal_error_callback(fatal_error_callback_type(self.__on_fatal_error_callback))
        self.__td_set_log_verbosity_level(int(verbosity))
        self.td_json_client = self.__td_json_client_create()

    def __on_fatal_error_callback(self, error_message: str) -> None:
        self.logger.error('TDLib fatal error: %s', error_message)

    def send(self, query: dict):
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        dumped_query = ujson.dumps(query, ensure_ascii=False).encode('utf-8')
        self.logger.debug(f'[me >>>] Sending {dumped_query}')
        self.__td_json_client_send(self.td_json_client, dumped_query)

    def execute(self, query: dict) -> typing.Optional[dict]:
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        dumped_query = ujson.dumps(query, ensure_ascii=False).encode('utf-8')
        self.logger.debug(f'Executing query {dumped_query} as client {self.td_json_client}')
        result = self.__td_json_client_execute(dumped_query)

        if result:
            result = ujson.loads(result)

        return result

    def receive(self, timeout: float = 10.0) -> typing.Optional[dict]:
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        result = self.__td_json_client_receive(timeout)

        if bool(result):
            self.logger.debug(f'[me <<<] Received {result}')
            result = ujson.loads(result)

            # Each returned object will have an "@client_id" field,
            # containing the identifier of the client for which a response or an update was received.
            if result.pop('@client_id', None) != self.td_json_client:
                return None

        return result

    def stop(self) -> None:
        # TDLib client instances are destroyed automatically after they are closed, so we need to send close
        self.send({'@type': 'close'})
