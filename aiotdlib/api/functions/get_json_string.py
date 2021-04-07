# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import JsonValue


class GetJsonString(BaseObject):
    """
    Converts a JsonValue object to corresponding JSON-serialized string. Can be called synchronously
    
    Params:
        json_value (:class:`JsonValue`)
            The JsonValue object
        
    """

    ID: str = Field("getJsonString", alias="@type")
    json_value: JsonValue

    @staticmethod
    def read(q: dict) -> GetJsonString:
        return GetJsonString.construct(**q)
