# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .proxy_type import ProxyType
from ..base_object import BaseObject


class Proxy(BaseObject):
    """
    Contains information about a proxy server
    
    Params:
        id (:class:`int`)
            Unique identifier of the proxy
        
        server (:class:`str`)
            Proxy server IP address
        
        port (:class:`int`)
            Proxy server port
        
        last_used_date (:class:`int`)
            Point in time (Unix timestamp) when the proxy was last used; 0 if never
        
        is_enabled (:class:`bool`)
            True, if the proxy is enabled now
        
        type_ (:class:`ProxyType`)
            Type of the proxy
        
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
