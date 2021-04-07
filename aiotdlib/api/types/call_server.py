# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .call_server_type import CallServerType
from ..base_object import BaseObject


class CallServer(BaseObject):
    """
    Describes a server for relaying call data
    
    Params:
        id (:class:`int`)
            Server identifier
        
        ip_address (:class:`str`)
            Server IPv4 address
        
        ipv6_address (:class:`str`)
            Server IPv6 address
        
        port (:class:`int`)
            Server port number
        
        type_ (:class:`CallServerType`)
            Server type
        
    """

    ID: str = Field("callServer", alias="@type")
    id: int
    ip_address: str
    ipv6_address: str
    port: int
    type_: CallServerType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> CallServer:
        return CallServer.construct(**q)
