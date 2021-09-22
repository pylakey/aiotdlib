# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Date(BaseObject):
    """
    Represents a date according to the Gregorian calendar
    
    :param day: Day of the month; 1-31
    :type day: :class:`int`
    
    :param month: Month; 1-12
    :type month: :class:`int`
    
    :param year: Year; 1-9999
    :type year: :class:`int`
    
    """

    ID: str = Field("date", alias="@type")
    day: int
    month: int
    year: int

    @staticmethod
    def read(q: dict) -> Date:
        return Date.construct(**q)
