from __future__ import annotations

import base64
import logging
import typing
from typing import Annotated, Any, Optional

import pydantic

INT32_MAX_VALUE = 2**31  # Unsigned INT32
INT53_MAX_VALUE = 2**52  # Unsigned INT53
INT64_MAX_VALUE = DOUBLE64_MAX_VALUE = 2**63  # Unsigned INT64
INT32_MIN_VALUE = -INT32_MAX_VALUE
INT53_MIN_VALUE = -INT53_MAX_VALUE
INT64_MIN_VALUE = DOUBLE64_MIN_VALUE = -INT64_MAX_VALUE

Bool = bool
String = str
Double = Annotated[float, pydantic.Field(gt=DOUBLE64_MIN_VALUE, lt=DOUBLE64_MAX_VALUE)]
Int32 = Annotated[int, pydantic.Field(gt=INT32_MIN_VALUE, lt=INT32_MAX_VALUE)]
Int53 = Annotated[int, pydantic.Field(gt=INT53_MIN_VALUE, lt=INT53_MAX_VALUE)]
Int64 = Annotated[int, pydantic.Field(gt=INT64_MIN_VALUE, lt=INT64_MAX_VALUE)]
Bytes = Annotated[
    typing.Union[str, bytes],
    pydantic.PlainSerializer(
        lambda v: base64.urlsafe_b64encode(v).decode(),
        return_type=str,
        when_used="json-unless-none",
    ),
    pydantic.BeforeValidator(
        lambda v: base64.urlsafe_b64decode(v.encode()) if isinstance(v, str) else v,
    ),
]
Vector = list

logger = logging.getLogger("BaseObject")


class BaseObject(pydantic.BaseModel):
    model_config = pydantic.ConfigDict(
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        use_enum_values=True,
        # populate_by_name=True,
    )

    EXTRA: Optional[dict[str, Any]] = pydantic.Field({}, alias="@extra", validation_alias="@extra")
