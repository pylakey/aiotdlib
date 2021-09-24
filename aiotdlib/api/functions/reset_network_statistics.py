# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResetNetworkStatistics(BaseObject):
    """
    Resets all network data usage statistics to zero. Can be called before authorization
    
    """

    ID: str = Field("resetNetworkStatistics", alias="@type")

    @staticmethod
    def read(q: dict) -> ResetNetworkStatistics:
        return ResetNetworkStatistics.construct(**q)
