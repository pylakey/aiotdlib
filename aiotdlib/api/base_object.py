from __future__ import annotations

import logging
from enum import Enum
from typing import Dict, Optional, Type

from pydantic import BaseConfig, BaseModel, Field

logger = logging.getLogger('BaseObject')


class BaseObject(BaseModel):
    class Config(BaseConfig):
        anystr_strip_whitespace = True
        validate_assignment = True
        underscore_attrs_are_private = True
        use_enum_values = True

    _all: Optional[Dict[str, Type[BaseObject]]] = {}
    ID: str = Field(..., alias='@type')

    @staticmethod
    def read(data: dict):
        if isinstance(data, (list, tuple,)):
            return [BaseObject.read(x) for x in data]

        if not isinstance(data, dict):
            return data

        q_type = data.get('@type')

        if not bool(q_type):
            logger.warning(f'@type not found in received update. {data}')
            return data

        q_type = q_type.value if isinstance(q_type, Enum) else q_type
        object_class = BaseObject._all.get(q_type)

        if not bool(object_class):
            logger.error(f'Object class not found for @type={q_type}')
            return data

        for key, value in data.items():
            data[key] = value if key == '@extra' else BaseObject.read(value)

        return object_class.read(data)
