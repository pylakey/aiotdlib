# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RemoveProxy(BaseObject):
    """
    Removes a proxy server. Can be called before authorization

    :param proxy_id: Proxy identifier
    :type proxy_id: :class:`Int32`
    """

    ID: typing.Literal["removeProxy"] = "removeProxy"
    proxy_id: Int32
