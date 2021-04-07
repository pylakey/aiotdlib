# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PingProxy(BaseObject):
    """
    Computes time needed to receive a response from a Telegram server through a proxy. Can be called before authorization
    
    Params:
        proxy_id (:class:`int`)
            Proxy identifier. Use 0 to ping a Telegram server without a proxy
        
    """

    ID: str = Field("pingProxy", alias="@type")
    proxy_id: int

    @staticmethod
    def read(q: dict) -> PingProxy:
        return PingProxy.construct(**q)
