import logging
import platform
import sys
import typing
from ctypes import *
from ctypes.util import find_library
from enum import IntEnum

import pkg_resources
import ujson

TDLIB_VERSION = '1.7.6'
TDLIB_MAX_INT = 2 ** 63 - 1
log_message_callback_type = CFUNCTYPE(None, c_int, c_char_p)


def _get_tdjson_lib_path() -> str:
    tdjson_path = find_library('tdjson')

    if tdjson_path is not None:
        return tdjson_path

    if platform.system().lower() == 'darwin':
        lib_name = f"libtdjson.{TDLIB_VERSION}.dylib"
    elif platform.system().lower() == 'windows':
        lib_name = f"libtdjson.{TDLIB_VERSION}.dll"
    else:
        # By default tdlib is built with this name
        lib_name = f"libtdjson.so.{TDLIB_VERSION}"

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
    __td_create_client_id: typing.Callable[[], int]
    __td_receive: typing.Callable[[float], bytes]
    __td_send: typing.Callable[[int, bytes], None]
    __td_execute: typing.Callable[[bytes], bytes]
    __td_set_log_verbosity_level: typing.Callable[[int], None]
    __td_set_log_message_callback: typing.Callable[[log_message_callback_type], None]

    td_json_client: typing.Optional[int] = None

    def __init__(self, library_path: str = None, verbosity: TDLibLogVerbosity = TDLibLogVerbosity.ERROR) -> None:
        if library_path is None:
            library_path = _get_tdjson_lib_path()

        if library_path is None:
            raise ValueError('Unable to find TD library binaries')

        self.logger = logging.getLogger(__name__)
        self.logger.info('Using shared library "%s"', library_path)
        self.initialize(library_path, verbosity)

    def __del__(self) -> None:
        try:
            self.stop()
        except:
            pass

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

        # td_set_log_verbosity_level
        self.__td_set_log_verbosity_level = self.__tdjson.td_set_log_verbosity_level
        self.__td_set_log_verbosity_level.restype = None
        self.__td_set_log_verbosity_level.argtypes = [c_int]

    def initialize(self, library_path: str, verbosity: TDLibLogVerbosity) -> None:
        self.inject_library(library_path)

        if bool(self.td_json_client):
            raise RuntimeError('TDJson instance is already initialized')

        self.__td_set_log_verbosity_level(int(verbosity))
        self.__td_set_log_message_callback(log_message_callback_type(self.__log_message_callback))
        self.td_json_client = self.__td_create_client_id()

    def send(self, query: dict):
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        dumped_query = ujson.dumps(query, ensure_ascii=False).encode('utf-8')
        self.logger.debug(f'[me >>>] Sending {dumped_query}')
        self.__td_send(self.td_json_client, dumped_query)

    def execute(self, query: dict) -> typing.Optional[dict]:
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        dumped_query = ujson.dumps(query, ensure_ascii=False).encode('utf-8')
        self.logger.debug(f'Executing query {dumped_query} as client {self.td_json_client}')
        result = self.__td_execute(dumped_query)

        if result:
            result = ujson.loads(result)

        return result

    def receive(self, timeout: float = 10.0) -> typing.Optional[dict]:
        if not bool(self.td_json_client):
            raise RuntimeError('Instance is not initialized')

        result = self.__td_receive(timeout)

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

    def __log_message_callback(self, verbosity_level: int, message: str) -> None:
        if verbosity_level == TDLibLogVerbosity.FATAL:
            self.logger.error('TDLib fatal error: %s', message)

        sys.stdout.flush()
