# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ProxyType
from ..base_object import BaseObject


class TestProxy(BaseObject):
    """
    Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization
    
    :param server: Proxy server IP address
    :type server: :class:`str`
    
    :param port: Proxy server port
    :type port: :class:`int`
    
    :param type_: Proxy type
    :type type_: :class:`ProxyType`
    
    :param dc_id: Identifier of a datacenter, with which to test connection
    :type dc_id: :class:`int`
    
    :param timeout: The maximum overall timeout for the request
    :type timeout: :class:`float`
    
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
