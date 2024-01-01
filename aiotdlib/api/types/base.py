from __future__ import annotations

import logging
import typing
from typing import Annotated
from typing import Any
from typing import Optional

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import Field

Bool = bool
Double = Annotated[float, Field(lt=2**64)]
String = str
Int32 = Annotated[int, Field(lt=2**32)]
Int53 = Annotated[int, Field(lt=2**53)]
Int64 = Annotated[int, Field(lt=2**64)]
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
