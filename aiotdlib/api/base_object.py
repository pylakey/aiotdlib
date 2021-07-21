from __future__ import annotations

import logging
from enum import Enum
from typing import (
    Any,
    Dict,
    Optional,
    Type,
)

import ujson
from pydantic import (
    BaseConfig,
    BaseModel,
    Field,
)

logger = logging.getLogger('BaseObject')


class BaseObject(BaseModel):
    class Config(BaseConfig):
        anystr_strip_whitespace = True
        underscore_attrs_are_private = True
        use_enum_values = True
        json_loads = ujson.loads

    _all: Optional[Dict[str, Type[BaseObject]]] = {}
    ID: str = Field(..., alias='@type')
    EXTRA: Optional[dict[str, Any]] = Field({}, alias='@extra')

    @staticmethod
    def read(data: dict):
        if isinstance(data, (list, tuple,)):
            return [BaseObject.read(x) for x in data]

        if not isinstance(data, dict):
            return data

        q_type = data.get('@type')

        if not bool(q_type):
            return data

        q_type = q_type.value if isinstance(q_type, Enum) else q_type
        object_class = BaseObject._all.get(q_type)

        if not bool(object_class):
            logger.error(f'Object class not found for @type={q_type}')
            return data

        processed_data = {}

        for key, value in data.items():
            # Workaround for BaseModel.construct(**kwargs).
            # It doesn't automatically rename fields according to aliases
            if key in ['json', 'filter', 'type', 'hash']:
                key = key + "_"
            elif key == '@extra':
                key = 'EXTRA'

            processed_data[key] = BaseObject.read(value)

        del data

        return object_class.read(processed_data)
