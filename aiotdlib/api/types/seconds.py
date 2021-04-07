# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Seconds(BaseObject):
    """
    Contains a value representing a number of seconds
    
    Params:
        seconds (:class:`float`)
            Number of seconds
        
    """

    ID: str = Field("seconds", alias="@type")
    seconds: float

    @staticmethod
    def read(q: dict) -> Seconds:
        return Seconds.construct(**q)
