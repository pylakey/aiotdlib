from __future__ import annotations

from typing import (
    Any,
    Callable,
    Coroutine,
    TypeVar,
)

from aiotdlib.api import BaseObject
from .handlers import HandlerCallable

SomeUpdate = TypeVar('SomeUpdate', bound=BaseObject)
MiddlewareCallable = Callable[['aiotdlib.Client', SomeUpdate, HandlerCallable], Coroutine[Any, Any, None]]
