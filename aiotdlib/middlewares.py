from __future__ import annotations

from typing import TYPE_CHECKING, Awaitable, Callable, TypeVar

from .api import BaseObject
from .handlers import HandlerCallable

if TYPE_CHECKING:
    from .client import Client

SomeUpdate = TypeVar("SomeUpdate", bound=BaseObject, covariant=True)
MiddlewareCallable = Callable[["Client", SomeUpdate, HandlerCallable], Awaitable[None]]
