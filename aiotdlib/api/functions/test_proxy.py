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


class TestProxy(BaseObject):
    """
    Sends a simple network request to the Telegram servers via proxy; for testing only. Can be called before authorization

    :param server: Proxy server domain or IP address
    :type server: :class:`String`
    :param port: Proxy server port
    :type port: :class:`Int32`
    :param type_: Proxy type
    :type type_: :class:`ProxyType`
    :param dc_id: Identifier of a datacenter with which to test connection
    :type dc_id: :class:`Int32`
    :param timeout: The maximum overall timeout for the request
    :type timeout: :class:`Double`
    """

    ID: typing.Literal["testProxy"] = "testProxy"
    server: String
    port: Int32
    type_: ProxyType = Field(..., alias="type")
    dc_id: Int32
    timeout: Double
