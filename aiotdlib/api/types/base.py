from __future__ import annotations

import logging
import typing
from typing import Annotated
from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

INT32_MAX_VALUE = 2 ** 32 - 1
INT53_MAX_VALUE = 2 ** 53 - 1
INT64_MAX_VALUE = DOUBLE64_MAX_VALUE = 2 ** 64 - 1

Bool = bool
String = str
Double = Annotated[float, Field(lt=DOUBLE64_MAX_VALUE)]
Int32 = Annotated[int, Field(le=INT32_MAX_VALUE)]
Int53 = Annotated[int, Field(le=INT53_MAX_VALUE)]
Int64 = Annotated[int, Field(le=INT64_MAX_VALUE)]
Bytes = typing.Union[str, bytes]
Vector = list

logger = logging.getLogger("BaseObject")


class BaseObject(BaseModel):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        str_strip_whitespace=True,
        use_enum_values=True,
        populate_by_name=True,
    )

    EXTRA: Optional[dict[str, Any]] = Field({}, alias="@extra")
