# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetProxies(BaseObject):
    """
    Returns list of proxies that are currently set up. Can be called before authorization
    
    """

    ID: str = Field("getProxies", alias="@type")

    @staticmethod
    def read(q: dict) -> GetProxies:
        return GetProxies.construct(**q)
