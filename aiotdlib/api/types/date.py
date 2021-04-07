# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Date(BaseObject):
    """
    Represents a date according to the Gregorian calendar
    
    Params:
        day (:class:`int`)
            Day of the month; 1-31
        
        month (:class:`int`)
            Month; 1-12
        
        year (:class:`int`)
            Year; 1-9999
        
    """

    ID: str = Field("date", alias="@type")
    day: int
    month: int
    year: int

    @staticmethod
    def read(q: dict) -> Date:
        return Date.construct(**q)
