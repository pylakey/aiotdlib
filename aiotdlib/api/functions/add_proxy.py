# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ProxyType


class AddProxy(BaseObject):
    """
    Adds a proxy server for network requests. Can be called before authorization
    
    :param server: Proxy server IP address
    :type server: :class:`str`
    
    :param port: Proxy server port
    :type port: :class:`int`
    
    :param enable: Pass true to immediately enable the proxy
    :type enable: :class:`bool`
    
    :param type_: Proxy type
    :type type_: :class:`ProxyType`
    
    """

    ID: str = Field("addProxy", alias="@type")
    server: str
    port: int
    enable: bool
    type_: ProxyType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> AddProxy:
        return AddProxy.construct(**q)
