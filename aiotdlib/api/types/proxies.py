# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .proxy import Proxy
from ..base_object import BaseObject


class Proxies(BaseObject):
    """
    Represents a list of proxy servers
    
    :param proxies: List of proxy servers
    :type proxies: :class:`list[Proxy]`
    
    """

    ID: str = Field("proxies", alias="@type")
    proxies: list[Proxy]

    @staticmethod
    def read(q: dict) -> Proxies:
        return Proxies.construct(**q)
