# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import NetworkStatisticsEntry


class AddNetworkStatistics(BaseObject):
    """
    Adds the specified data to data usage statistics. Can be called before authorization
    
    Params:
        entry (:class:`NetworkStatisticsEntry`)
            The network statistics entry with the data to be added to statistics
        
    """

    ID: str = Field("addNetworkStatistics", alias="@type")
    entry: NetworkStatisticsEntry

    @staticmethod
    def read(q: dict) -> AddNetworkStatistics:
        return AddNetworkStatistics.construct(**q)
