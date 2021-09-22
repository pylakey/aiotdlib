# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .network_statistics_entry import NetworkStatisticsEntry
from ..base_object import BaseObject


class NetworkStatistics(BaseObject):
    """
    A full list of available network statistic entries
    
    :param since_date: Point in time (Unix timestamp) from which the statistics are collected
    :type since_date: :class:`int`
    
    :param entries: Network statistics entries
    :type entries: :class:`list[NetworkStatisticsEntry]`
    
    """

    ID: str = Field("networkStatistics", alias="@type")
    since_date: int
    entries: list[NetworkStatisticsEntry]

    @staticmethod
    def read(q: dict) -> NetworkStatistics:
        return NetworkStatistics.construct(**q)
