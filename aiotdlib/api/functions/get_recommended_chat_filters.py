# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetRecommendedChatFilters(BaseObject):
    """
    Returns recommended chat filters for the current user
    
    """

    ID: str = Field("getRecommendedChatFilters", alias="@type")

    @staticmethod
    def read(q: dict) -> GetRecommendedChatFilters:
        return GetRecommendedChatFilters.construct(**q)
