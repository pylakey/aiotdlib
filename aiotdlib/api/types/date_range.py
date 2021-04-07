# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DateRange(BaseObject):
    """
    Represents a date range
    
    Params:
        start_date (:class:`int`)
            Point in time (Unix timestamp) at which the date range begins
        
        end_date (:class:`int`)
            Point in time (Unix timestamp) at which the date range ends
        
    """

    ID: str = Field("dateRange", alias="@type")
    start_date: int
    end_date: int

    @staticmethod
    def read(q: dict) -> DateRange:
        return DateRange.construct(**q)
