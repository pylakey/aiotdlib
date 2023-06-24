# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetProxyLink(BaseObject):
    """
    Returns an HTTPS link, which can be used to add a proxy. Available only for SOCKS5 and MTProto proxies. Can be called before authorization

    :param proxy_id: Proxy identifier
    :type proxy_id: :class:`Int32`
    """

    ID: typing.Literal["getProxyLink"] = "getProxyLink"
    proxy_id: Int32
