# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    ProxyType,
)


class AddProxy(BaseObject):
    """
    Adds a proxy server for network requests. Can be called before authorization

    :param server: Proxy server domain or IP address
    :type server: :class:`String`
    :param port: Proxy server port
    :type port: :class:`Int32`
    :param type_: Proxy type
    :type type_: :class:`ProxyType`
    :param enable: Pass true to immediately enable the proxy
    :type enable: :class:`Bool`
    """

    ID: typing.Literal["addProxy"] = "addProxy"
    server: String
    port: Int32
    type_: ProxyType = Field(..., alias="type")
    enable: Bool = False
