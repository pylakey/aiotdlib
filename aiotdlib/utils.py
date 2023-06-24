import asyncio
import base64
import getpass
import logging
import os
import re
import sys
import typing
from enum import Enum
from functools import partial
from typing import (
    Optional,
    TYPE_CHECKING,
    Union,
)

import ujson

from .api import (
    BaseObject,
    Error,
    InputFileId,
    InputFileLocal,
    InputFileRemote,
    InputThumbnail,
    TDLibObject,
    TDLibObjects,
)
from .api.errors import AioTDLibError
from .api.errors.error import http_code_to_error

if TYPE_CHECKING:
    from .client import Client

logger = logging.getLogger(__name__)
Query = typing.Union[str, bytes, dict]


async def ainput(prompt: str = "", secured: bool = False) -> str:
    if len(prompt):
        prompt = prompt.strip() + " "

    if secured:
        getpass_func = partial(getpass.getpass, prompt=prompt)
        stdin = await asyncio.get_event_loop().run_in_executor(None, getpass_func)
    else:
        print(prompt, end=" ", flush=True)
        stdin = await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)

    return stdin.strip()


def str_to_base64(text: Union[str, bytes]) -> str:
    if not text:
        return ''

    result = text

    if isinstance(result, str):
        result = result.encode()

    return base64.b64encode(result).decode()


def strip_phone_number_symbols(phone_number: str) -> str:
    if not isinstance(phone_number, str):
        try:
            phone_number = str(phone_number)
        except ValueError:
            raise ValueError(f'Phone number should be an instance of str, not a {phone_number.__class__.__name__}')

    return re.sub(r'(?<!^)|[^\d]+', '', phone_number)


def make_input_file(file: Union[str, int]) -> Union[InputFileId, InputFileLocal, InputFileRemote]:
    if os.path.exists(file):
        return InputFileLocal(path=file)
    elif isinstance(file, int):
        return InputFileId(id=file)

    return InputFileRemote(id=file)


def make_thumbnail(thumbnail: str, width: int = None, height: int = None) -> Optional[InputThumbnail]:
    if isinstance(thumbnail, str):
        return InputThumbnail.construct(
            # Sending thumbnails by file_id is currently not supported
            thumbnail=InputFileLocal(path=thumbnail),
            width=width,
            height=height,
        )

    return None


def encode_query(query: Query) -> bytes:
    if isinstance(query, dict):
        return ujson.dumps(query, ensure_ascii=False).encode('utf-8')
    elif isinstance(query, str):
        return query.encode('utf-8')
    elif isinstance(query, bytes):
        return query

    raise ValueError('Query has wrong type')


def parse_tdlib_object(data: dict) -> TDLibObject:
    if isinstance(data, (list, tuple,)):
        return [parse_tdlib_object(x) for x in data]

    if not isinstance(data, dict):
        return data

    type_ = data.get('@type')

    if not bool(type_):
        logger.error(f"Data: {data}")
        return data

    type_ = type_.value if isinstance(type_, Enum) else type_
    object_class = TDLibObjects.get(type_)

    if not bool(object_class):
        logger.error(f'Object class not found for @type={type_}')
        return data

    processed_data = {}

    for key, value in data.items():
        # Workaround for BaseModel.construct(**kwargs).
        # It doesn't automatically rename fields according to aliases
        if key in ['json', 'filter', 'type', 'hash']:
            key = key + "_"
        elif key == '@extra':
            key = 'EXTRA'
            processed_data[key] = value
            continue

        processed_data[key] = parse_tdlib_object(value)

    return object_class(**data)


class PendingRequest:
    request: Optional[TDLibObject] = None
    update: Optional[TDLibObject] = None
    error: bool = False

    def __init__(self, client: 'Client', request: TDLibObject) -> None:
        self.client = client
        self.request = request
        self.__ready_event = asyncio.Event()

    @property
    def id(self) -> Optional[str]:
        return self.request.EXTRA.get('request_id')

    async def wait(self, timeout: Union[int, float] = None, raise_exc: bool = False) -> None:
        result = await asyncio.wait_for(self.__ready_event.wait(), timeout=timeout)

        if result is False:
            raise asyncio.TimeoutError()

        if raise_exc and self.error:
            self.raise_error()

    def set_update(self, update: BaseObject):
        if isinstance(update, Error):
            self.error = True

        self.update = update
        self.__ready_event.set()

    def raise_error(self):
        if isinstance(self.update, Error):
            http_error = http_code_to_error.get(self.update.code, AioTDLibError)
            raise http_error(
                code=self.update.code,
                message=self.update.message
            )

        raise RuntimeError(f'Unknown TDLib error')
