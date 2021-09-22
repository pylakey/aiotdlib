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


class EditProxy(BaseObject):
    """
    Edits an existing proxy server for network requests. Can be called before authorization
    
    :param proxy_id: Proxy identifier
    :type proxy_id: :class:`int`
    
    :param server: Proxy server IP address
    :type server: :class:`str`
    
    :param port: Proxy server port
    :type port: :class:`int`
    
    :param enable: True, if the proxy should be enabled
    :type enable: :class:`bool`
    
    :param type_: Proxy type
    :type type_: :class:`ProxyType`
    
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
