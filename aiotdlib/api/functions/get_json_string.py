# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    JsonValue,
)


class GetJsonString(BaseObject):
    """
    Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously

    :param json_value: The JsonValue object
    :type json_value: :class:`JsonValue`
    """

    ID: typing.Literal["getJsonString"] = "getJsonString"
    json_value: JsonValue
