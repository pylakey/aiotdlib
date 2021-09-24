# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetRecentInlineBots(BaseObject):
    """
    Returns up to 20 recently used inline bots in the order of their last usage
    
    """

    ID: str = Field("getRecentInlineBots", alias="@type")

    @staticmethod
    def read(q: dict) -> GetRecentInlineBots:
        return GetRecentInlineBots.construct(**q)
