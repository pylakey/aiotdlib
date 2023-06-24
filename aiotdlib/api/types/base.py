from __future__ import annotations

import logging
import typing
from typing import (
    Any,
    Optional,
)

import pydantic
from pydantic import (
    BaseConfig,
    BaseModel,
    Field,
)

Bool = bool
Double = pydantic.confloat(lt=2**64)
String = str
Int32 = pydantic.conint(lt=2**32)
Int53 = pydantic.conint(lt=2**53)
Int64 = pydantic.conint(lt=2**64)
Bytes = typing.Union[str, bytes]
Vector = list

ArgumentType = typing.Union[Bool, Double, String, Int32, Int53, Int64, Bytes, Vector]

logger = logging.getLogger("BaseObject")


class BaseObject(BaseModel):
    class Config(BaseConfig):
        arbitrary_types_allowed = True
        anystr_strip_whitespace = True
        underscore_attrs_are_private = True
        use_enum_values = True
        allow_population_by_field_name = True
        fields = {"ID": {"default_value": None, "alias": "@type"}}

    EXTRA: Optional[dict[str, Any]] = Field({}, alias="@extra")
