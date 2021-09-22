# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetAlarm(BaseObject):
    """
    Succeeds after a specified amount of time has passed. Can be called before initialization
    
    :param seconds: Number of seconds before the function returns
    :type seconds: :class:`float`
    
    """

    ID: str = Field("setAlarm", alias="@type")
    seconds: float

    @staticmethod
    def read(q: dict) -> SetAlarm:
        return SetAlarm.construct(**q)
