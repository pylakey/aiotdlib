# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetJsonValue(BaseObject):
    """
    Converts a JSON-serialized string to corresponding JsonValue object. Can be called synchronously
    
    Params:
        json_ (:class:`str`)
            The JSON-serialized string
        
    """

    ID: str = Field("getJsonValue", alias="@type")
    json_: str = Field(..., alias='json')

    @staticmethod
    def read(q: dict) -> GetJsonValue:
        return GetJsonValue.construct(**q)
