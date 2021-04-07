# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class StatisticalValue(BaseObject):
    """
    A value with information about its recent changes
    
    Params:
        value (:class:`float`)
            The current value
        
        previous_value (:class:`float`)
            The value for the previous day
        
        growth_rate_percentage (:class:`float`)
            The growth rate of the value, as a percentage
        
    """

    ID: str = Field("statisticalValue", alias="@type")
    value: float
    previous_value: float
    growth_rate_percentage: float

    @staticmethod
    def read(q: dict) -> StatisticalValue:
        return StatisticalValue.construct(**q)
