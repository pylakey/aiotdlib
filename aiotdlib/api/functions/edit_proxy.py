# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ProxyType


class EditProxy(BaseObject):
    """
    Edits an existing proxy server for network requests. Can be called before authorization
    
    Params:
        proxy_id (:class:`int`)
            Proxy identifier
        
        server (:class:`str`)
            Proxy server IP address
        
        port (:class:`int`)
            Proxy server port
        
        enable (:class:`bool`)
            True, if the proxy should be enabled
        
        type_ (:class:`ProxyType`)
            Proxy type
        
    """

    ID: str = Field("editProxy", alias="@type")
    proxy_id: int
    server: str
    port: int
    enable: bool
    type_: ProxyType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> EditProxy:
        return EditProxy.construct(**q)
