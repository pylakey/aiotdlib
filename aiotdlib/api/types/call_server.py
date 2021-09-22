# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .call_server_type import CallServerType
from ..base_object import BaseObject


class CallServer(BaseObject):
    """
    Describes a server for relaying call data
    
    :param id: Server identifier
    :type id: :class:`int`
    
    :param ip_address: Server IPv4 address
    :type ip_address: :class:`str`
    
    :param ipv6_address: Server IPv6 address
    :type ipv6_address: :class:`str`
    
    :param port: Server port number
    :type port: :class:`int`
    
    :param type_: Server type
    :type type_: :class:`CallServerType`
    
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
