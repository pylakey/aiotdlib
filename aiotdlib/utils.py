from __future__ import annotations

import asyncio
import base64
import getpass
import logging
import os
import re
import sys
from enum import Enum
from functools import wraps
from time import perf_counter
from typing import TYPE_CHECKING, Optional, Union

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


def _read_input(prompt: str = "") -> str:
    print(prompt, end=" ", flush=True)
    return sys.stdin.readline()


async def ainput(prompt: str = "", secured: bool = False) -> str:
    if len(prompt):
        prompt = prompt.strip()

    if secured:
        stdin = await asyncio.to_thread(getpass.getpass, prompt=prompt, stream=None)
    else:
        stdin = await asyncio.to_thread(_read_input, prompt)

    return stdin.strip()


def str_to_base64(text: Union[str, bytes]) -> str:
    if not text:
        return ""

    result = text

    if isinstance(result, str):
        result = result.encode()

    return base64.b64encode(result).decode()


def strip_phone_number_symbols(phone_number: str) -> str:
    if not isinstance(phone_number, str):
        try:
            phone_number = str(phone_number)
        except ValueError as e:
            raise ValueError(
                f"Phone number should be an instance of str, not a {phone_number.__class__.__name__}"
            ) from e

    return re.sub(r"(?<!^)|[^\d]+", "", phone_number)


def make_input_file(file: Union[str, int]) -> Union[InputFileId, InputFileLocal, InputFileRemote]:
    if os.path.exists(file):
        return InputFileLocal(path=file)
    elif isinstance(file, int):
        return InputFileId(id=file)

    return InputFileRemote(id=file)


def make_thumbnail(thumbnail: str, width: int = 0, height: int = 0) -> Optional[InputThumbnail]:
    if isinstance(thumbnail, str):
        return InputThumbnail(
            # Sending thumbnails by file_id is currently not supported
            thumbnail=InputFileLocal(path=thumbnail),
            width=width,
            height=height,
        )

    return None


def parse_tdlib_object(data: dict) -> TDLibObject:
    if isinstance(
        data,
        (
            list,
            tuple,
        ),
    ):
        return [parse_tdlib_object(x) for x in data]

    if not isinstance(data, dict):
        return data

    type_ = data.get("@type")

    if not bool(type_):
        logger.error(f"Data: {data}")
        return data

    type_ = type_.value if isinstance(type_, Enum) else type_
    object_class = TDLibObjects.get(type_)

    if not bool(object_class):
        logger.error(f"Object class not found for @type={type_}")
        return data

    return object_class.model_validate(data)


class PendingRequest:
    def __init__(self, client: "Client", request: TDLibObject) -> None:
        self.client = client
        self.request: Optional[TDLibObject] = request
        self.update: Optional[TDLibObject] = None
        self.error: bool = False
        self._ready_event = asyncio.Event()

    @property
    def id(self) -> Optional[str]:
        return self.request.EXTRA.get("request_id")

    async def wait(self, timeout: Union[int, float] = None, raise_exc: bool = False) -> None:
        result = await asyncio.wait_for(self._ready_event.wait(), timeout=timeout)

        if result is False:
            raise asyncio.TimeoutError()

        if raise_exc and self.error:
            self.raise_error()

    def set_update(self, update: BaseObject):
        if isinstance(update, Error):
            self.error = True

        self.update = update
        self._ready_event.set()

    def raise_error(self):
        if isinstance(self.update, Error):
            http_error = http_code_to_error.get(self.update.code, AioTDLibError)
            raise http_error(code=self.update.code, message=self.update.message)

        raise RuntimeError(f"Unknown TDLib error: {type(self.update)}")


def measure_time(func: callable):
    _logger = logging.getLogger(f"{__name__}.'measure_time'")
    func_name = getattr(func, "__qualname__", "") or getattr(func, "__name__", "???")

    @wraps(func)
    async def decorated(*args, **kwargs):
        start_time = perf_counter()

        try:
            return await func(*args, **kwargs)
        except Exception as e:
            _logger.error(f"{func_name} call failed: {e}")
            raise e
        finally:
            end_time = perf_counter() - start_time
            logger.info(f"{func_name} call finished in {end_time} seconds")

    return decorated
