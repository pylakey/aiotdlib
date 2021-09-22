# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class StatisticalValue(BaseObject):
    """
    A value with information about its recent changes
    
    :param value: The current value
    :type value: :class:`float`
    
    :param previous_value: The value for the previous day
    :type previous_value: :class:`float`
    
    :param growth_rate_percentage: The growth rate of the value, as a percentage
    :type growth_rate_percentage: :class:`float`
    
    """

    ID: str = Field("statisticalValue", alias="@type")
    value: float
    previous_value: float
    growth_rate_percentage: float

    @staticmethod
    def read(q: dict) -> StatisticalValue:
        return StatisticalValue.construct(**q)
