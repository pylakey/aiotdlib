# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import NetworkStatisticsEntry
from ..base_object import BaseObject


class AddNetworkStatistics(BaseObject):
    """
    Adds the specified data to data usage statistics. Can be called before authorization
    
    :param entry: The network statistics entry with the data to be added to statistics
    :type entry: :class:`NetworkStatisticsEntry`
    
    """

    ID: str = Field("addNetworkStatistics", alias="@type")
    entry: NetworkStatisticsEntry

    @staticmethod
    def read(q: dict) -> AddNetworkStatistics:
        return AddNetworkStatistics.construct(**q)
