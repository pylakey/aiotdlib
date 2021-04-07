# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ProxyType


class TestProxy(BaseObject):
    """
    Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization
    
    Params:
        server (:class:`str`)
            Proxy server IP address
        
        port (:class:`int`)
            Proxy server port
        
        type_ (:class:`ProxyType`)
            Proxy type
        
        dc_id (:class:`int`)
            Identifier of a datacenter, with which to test connection
        
        timeout (:class:`float`)
            The maximum overall timeout for the request
        
    """

    ID: str = Field("testProxy", alias="@type")
    server: str
    port: int
    type_: ProxyType = Field(..., alias='type')
    dc_id: int
    timeout: float

    @staticmethod
    def read(q: dict) -> TestProxy:
        return TestProxy.construct(**q)
