# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ConnectionState(BaseObject):
    """
    Describes the current state of the connection to Telegram servers
    
    """

    ID: str = Field("connectionState", alias="@type")


class ConnectionStateConnecting(ConnectionState):
    """
    Currently establishing a connection to the Telegram servers
    
    """

    ID: str = Field("connectionStateConnecting", alias="@type")

    @staticmethod
    def read(q: dict) -> ConnectionStateConnecting:
        return ConnectionStateConnecting.construct(**q)


class ConnectionStateConnectingToProxy(ConnectionState):
    """
    Currently establishing a connection with a proxy server
    
    """

    ID: str = Field("connectionStateConnectingToProxy", alias="@type")

    @staticmethod
    def read(q: dict) -> ConnectionStateConnectingToProxy:
        return ConnectionStateConnectingToProxy.construct(**q)


class ConnectionStateReady(ConnectionState):
    """
    There is a working connection to the Telegram servers
    
    """

    ID: str = Field("connectionStateReady", alias="@type")

    @staticmethod
    def read(q: dict) -> ConnectionStateReady:
        return ConnectionStateReady.construct(**q)


class ConnectionStateUpdating(ConnectionState):
    """
    Downloading data received while the application was offline
    
    """

    ID: str = Field("connectionStateUpdating", alias="@type")

    @staticmethod
    def read(q: dict) -> ConnectionStateUpdating:
        return ConnectionStateUpdating.construct(**q)


class ConnectionStateWaitingForNetwork(ConnectionState):
    """
    Currently waiting for the network to become available. Use setNetworkType to change the available network type
    
    """

    ID: str = Field("connectionStateWaitingForNetwork", alias="@type")

    @staticmethod
    def read(q: dict) -> ConnectionStateWaitingForNetwork:
        return ConnectionStateWaitingForNetwork.construct(**q)
