from __future__ import annotations

import logging
import typing
from typing import Annotated
from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

INT32_MAX_VALUE = 2**31  # Unsigned INT32
INT53_MAX_VALUE = 2**52  # Unsigned INT53
INT64_MAX_VALUE = DOUBLE64_MAX_VALUE = 2**63  # Unsigned INT64
INT32_MIN_VALUE = -INT32_MAX_VALUE
INT53_MIN_VALUE = -INT53_MAX_VALUE
INT64_MIN_VALUE = DOUBLE64_MIN_VALUE = -INT64_MAX_VALUE

Bool = bool
String = str
Double = Annotated[float, Field(gt=DOUBLE64_MIN_VALUE, lt=DOUBLE64_MAX_VALUE)]
Int32 = Annotated[int, Field(gt=INT32_MIN_VALUE, lt=INT32_MAX_VALUE)]
Int53 = Annotated[int, Field(gt=INT53_MIN_VALUE, lt=INT53_MAX_VALUE)]
Int64 = Annotated[int, Field(gt=INT64_MIN_VALUE, lt=INT64_MAX_VALUE)]
Bytes = typing.Union[str, bytes]
Vector = list

logger = logging.getLogger("BaseObject")


class BaseObject(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        use_enum_values=True,
        # populate_by_name=True,
    )

    EXTRA: Optional[dict[str, Any]] = Field({}, alias="@extra", validation_alias="@extra")
