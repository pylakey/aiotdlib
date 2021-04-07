# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class NetworkType(BaseObject):
    """
    Represents the type of a network
    
    """

    ID: str = Field("networkType", alias="@type")


class NetworkTypeMobile(NetworkType):
    """
    A mobile network
    
    """

    ID: str = Field("networkTypeMobile", alias="@type")

    @staticmethod
    def read(q: dict) -> NetworkTypeMobile:
        return NetworkTypeMobile.construct(**q)


class NetworkTypeMobileRoaming(NetworkType):
    """
    A mobile roaming network
    
    """

    ID: str = Field("networkTypeMobileRoaming", alias="@type")

    @staticmethod
    def read(q: dict) -> NetworkTypeMobileRoaming:
        return NetworkTypeMobileRoaming.construct(**q)


class NetworkTypeNone(NetworkType):
    """
    The network is not available
    
    """

    ID: str = Field("networkTypeNone", alias="@type")

    @staticmethod
    def read(q: dict) -> NetworkTypeNone:
        return NetworkTypeNone.construct(**q)


class NetworkTypeOther(NetworkType):
    """
    A different network type (e.g., Ethernet network)
    
    """

    ID: str = Field("networkTypeOther", alias="@type")

    @staticmethod
    def read(q: dict) -> NetworkTypeOther:
        return NetworkTypeOther.construct(**q)


class NetworkTypeWiFi(NetworkType):
    """
    A Wi-Fi network
    
    """

    ID: str = Field("networkTypeWiFi", alias="@type")

    @staticmethod
    def read(q: dict) -> NetworkTypeWiFi:
        return NetworkTypeWiFi.construct(**q)
