# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetProxyLink(BaseObject):
    """
    Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization
    
    Params:
        proxy_id (:class:`int`)
            Proxy identifier
        
    """

    ID: str = Field("getProxyLink", alias="@type")
    proxy_id: int

    @staticmethod
    def read(q: dict) -> GetProxyLink:
        return GetProxyLink.construct(**q)
