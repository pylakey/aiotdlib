# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetJsonValue(BaseObject):
    """
    Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously

    :param json_: The JSON-serialized string
    :type json_: :class:`String`
    """

    ID: typing.Literal["getJsonValue"] = "getJsonValue"
    json_: String = Field(..., alias="json")
