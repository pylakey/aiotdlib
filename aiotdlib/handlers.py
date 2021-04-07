from __future__ import annotations

import asyncio
from collections.abc import Callable
from typing import Any, Coroutine, Optional, TypeVar

from .api import BaseObject
from .filters import FilterCallable

SomeUpdate = TypeVar('SomeUpdate', bound=BaseObject)
HandlerCallable = Callable[['aiotdlib.Client', SomeUpdate], Coroutine[Any, Any, None]]


class Handler(object):
    def __init__(self, function: HandlerCallable, *, filters: FilterCallable = None):
        if not asyncio.iscoroutinefunction(function):
            raise ValueError('function should be async callable!')

        if filters is not None and not asyncio.iscoroutinefunction(filters):
            raise ValueError('filters should be async callable!')

        self.function: HandlerCallable = function
        self.filters: Optional[FilterCallable] = filters

    async def __call__(self, client: 'Client', update: BaseObject):
        if callable(self.filters):
            filter_result = await self.filters(update)

            if not filter_result:
                return

        return await self.function(client, update)
