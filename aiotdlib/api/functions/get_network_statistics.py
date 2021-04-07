# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetNetworkStatistics(BaseObject):
    """
    Returns network data usage statistics. Can be called before authorization
    
    Params:
        only_current (:class:`bool`)
            If true, returns only data for the current library launch
        
    """

    ID: str = Field("getNetworkStatistics", alias="@type")
    only_current: bool

    @staticmethod
    def read(q: dict) -> GetNetworkStatistics:
        return GetNetworkStatistics.construct(**q)
