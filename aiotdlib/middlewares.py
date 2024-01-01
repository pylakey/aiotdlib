from __future__ import annotations

from typing import Awaitable
from typing import Callable
from typing import TypeVar

from .api import BaseObject
from .handlers import HandlerCallable

SomeUpdate = TypeVar('SomeUpdate', bound=BaseObject)
MiddlewareCallable = Callable[['aiotdlib.Client', SomeUpdate, HandlerCallable], Awaitable[None]]
