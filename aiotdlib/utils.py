import asyncio
import base64
import getpass
import logging
import sys
from functools import partial
from typing import (
    Optional,
    TYPE_CHECKING,
    Union,
)

from .api import (
    BaseObject,
    Error,
)
from .api.errors import (
    AioTDLibError,
    Unauthorized,
)

if TYPE_CHECKING:
    from .client import Client

logger = logging.getLogger(__name__)


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


class PendingRequest:
    request: Optional[BaseObject] = None
    update: Optional[BaseObject] = None
    error: bool = False

    def __init__(self, client: 'Client', request: BaseObject) -> None:
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
            if self.update.code == 401:
                raise Unauthorized(self.update.message)

            raise AioTDLibError(self.update.code, self.update.message)

        raise RuntimeError(f'Unknown TDLib error')
