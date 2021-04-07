# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        network_type (:class:`NetworkType`)
            Type of the network the data was sent through. Call setNetworkType to maintain the actual network type
        
        sent_bytes (:class:`int`)
            Total number of bytes sent
        
        received_bytes (:class:`int`)
            Total number of bytes received
        
        duration (:class:`float`)
            Total call duration, in seconds
        
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
    
    Params:
        file_type (:class:`FileType`)
            Type of the file the data is part of
        
        network_type (:class:`NetworkType`)
            Type of the network the data was sent through. Call setNetworkType to maintain the actual network type
        
        sent_bytes (:class:`int`)
            Total number of bytes sent
        
        received_bytes (:class:`int`)
            Total number of bytes received
        
    """

    ID: str = Field("networkStatisticsEntryFile", alias="@type")
    file_type: FileType
    network_type: NetworkType
    sent_bytes: int
    received_bytes: int

    @staticmethod
    def read(q: dict) -> NetworkStatisticsEntryFile:
        return NetworkStatisticsEntryFile.construct(**q)
