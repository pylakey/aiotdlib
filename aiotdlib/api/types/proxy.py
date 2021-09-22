# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .proxy_type import ProxyType
from ..base_object import BaseObject


class Proxy(BaseObject):
    """
    Contains information about a proxy server
    
    :param id: Unique identifier of the proxy
    :type id: :class:`int`
    
    :param server: Proxy server IP address
    :type server: :class:`str`
    
    :param port: Proxy server port
    :type port: :class:`int`
    
    :param last_used_date: Point in time (Unix timestamp) when the proxy was last used; 0 if never
    :type last_used_date: :class:`int`
    
    :param is_enabled: True, if the proxy is enabled now
    :type is_enabled: :class:`bool`
    
    :param type_: Type of the proxy
    :type type_: :class:`ProxyType`
    
    """

    ID: str = Field("proxy", alias="@type")
    id: int
    server: str
    port: int
    last_used_date: int
    is_enabled: bool
    type_: ProxyType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> Proxy:
        return Proxy.construct(**q)
