from collections import Callable, Coroutine
from typing import Any

from aiotdlib.api import BaseObject, MessageText, UpdateNewMessage

FilterCallable = Callable[[BaseObject], Coroutine[Any, Any, bool]]


# Some predefined filters
async def text_message(update: BaseObject):
    return isinstance(update, UpdateNewMessage) and isinstance(update.message.content, MessageText)
