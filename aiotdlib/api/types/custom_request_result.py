# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CustomRequestResult(BaseObject):
    """
    Contains the result of a custom request
    
    Params:
        result (:class:`str`)
            A JSON-serialized result
        
    """

    ID: str = Field("customRequestResult", alias="@type")
    result: str

    @staticmethod
    def read(q: dict) -> CustomRequestResult:
        return CustomRequestResult.construct(**q)
