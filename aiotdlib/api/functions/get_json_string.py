# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import JsonValue
from ..base_object import BaseObject


class GetJsonString(BaseObject):
    """
    Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously
    
    :param json_value: The JsonValue object
    :type json_value: :class:`JsonValue`
    
    """

    ID: str = Field("getJsonString", alias="@type")
    json_value: JsonValue

    @staticmethod
    def read(q: dict) -> GetJsonString:
        return GetJsonString.construct(**q)
