# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RemoveProxy(BaseObject):
    """
    Removes a proxy server. Can be called before authorization
    
    :param proxy_id: Proxy identifier
    :type proxy_id: :class:`int`
    
    """

    ID: str = Field("removeProxy", alias="@type")
    proxy_id: int

    @staticmethod
    def read(q: dict) -> RemoveProxy:
        return RemoveProxy.construct(**q)
