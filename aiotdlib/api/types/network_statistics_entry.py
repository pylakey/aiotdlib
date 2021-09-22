# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file_type import FileType
from .network_type import NetworkType
from ..base_object import BaseObject


class NetworkStatisticsEntry(BaseObject):
    """
    Contains statistics about network usage
    
    """

    ID: str = Field("networkStatisticsEntry", alias="@type")


class NetworkStatisticsEntryCall(NetworkStatisticsEntry):
    """
    Contains information about the total amount of data that was used for calls
    
    :param network_type: Type of the network the data was sent through. Call setNetworkType to maintain the actual network type
    :type network_type: :class:`NetworkType`
    
    :param sent_bytes: Total number of bytes sent
    :type sent_bytes: :class:`int`
    
    :param received_bytes: Total number of bytes received
    :type received_bytes: :class:`int`
    
    :param duration: Total call duration, in seconds
    :type duration: :class:`float`
    
    """

    ID: str = Field("networkStatisticsEntryCall", alias="@type")
    network_type: NetworkType
    sent_bytes: int
    received_bytes: int
    duration: float

    @staticmethod
    def read(q: dict) -> NetworkStatisticsEntryCall:
        return NetworkStatisticsEntryCall.construct(**q)


class NetworkStatisticsEntryFile(NetworkStatisticsEntry):
    """
    Contains information about the total amount of data that was used to send and receive files
    
    :param file_type: Type of the file the data is part of
    :type file_type: :class:`FileType`
    
    :param network_type: Type of the network the data was sent through. Call setNetworkType to maintain the actual network type
    :type network_type: :class:`NetworkType`
    
    :param sent_bytes: Total number of bytes sent
    :type sent_bytes: :class:`int`
    
    :param received_bytes: Total number of bytes received
    :type received_bytes: :class:`int`
    
    """

    ID: str = Field("networkStatisticsEntryFile", alias="@type")
    file_type: FileType
    network_type: NetworkType
    sent_bytes: int
    received_bytes: int

    @staticmethod
    def read(q: dict) -> NetworkStatisticsEntryFile:
        return NetworkStatisticsEntryFile.construct(**q)
