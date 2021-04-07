# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetAlarm(BaseObject):
    """
    Succeeds after a specified amount of time has passed. Can be called before initialization
    
    Params:
        seconds (:class:`float`)
            Number of seconds before the function returns
        
    """

    ID: str = Field("setAlarm", alias="@type")
    seconds: float

    @staticmethod
    def read(q: dict) -> SetAlarm:
        return SetAlarm.construct(**q)
