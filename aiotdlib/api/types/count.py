# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Count(BaseObject):
    """
    Contains a counter
    
    Params:
        count (:class:`int`)
            Count
        
    """

    ID: str = Field("count", alias="@type")
    count: int

    @staticmethod
    def read(q: dict) -> Count:
        return Count.construct(**q)
