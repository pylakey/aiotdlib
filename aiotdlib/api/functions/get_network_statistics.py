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
    
    :param only_current: Pass true to get statistics only for the current library launch
    :type only_current: :class:`bool`
    
    """

    ID: str = Field("getNetworkStatistics", alias="@type")
    only_current: bool

    @staticmethod
    def read(q: dict) -> GetNetworkStatistics:
        return GetNetworkStatistics.construct(**q)
