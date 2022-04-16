from __future__ import annotations

import asyncio
from typing import (
    Any,
    Callable,
    Coroutine,
    Optional,
    TYPE_CHECKING,
    TypeVar,
    Union,
)

from .api import BaseObject
from .filters import (
    BaseFilter,
    FilterCallable,
)

if TYPE_CHECKING:
    from client import Client

SomeUpdate = TypeVar('SomeUpdate', bound=BaseObject)
HandlerCallable = Callable[['Client', SomeUpdate], Coroutine[Any, Any, None]]


class Handler(object):
    def __init__(self, function: HandlerCallable, *, filters: Union[BaseFilter, FilterCallable] = None):
        if filters is not None and not isinstance(filters, BaseFilter) and not asyncio.iscoroutinefunction(function):
            raise ValueError('filters should be an instance of BaseFilter!')

        self.function: HandlerCallable = function
        self.filters: Optional[FilterCallable] = filters

    async def __call__(self, client: 'Client', update: BaseObject):
        if callable(self.filters):
            filter_result = await self.filters(update)

            if not bool(filter_result):
                return

            if isinstance(filter_result, dict):
                update.EXTRA |= filter_result

        return await self.function(client, update)
