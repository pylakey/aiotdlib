# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_filter import ChatFilter
from ..base_object import BaseObject


class RecommendedChatFilter(BaseObject):
    """
    Describes a recommended chat filter
    
    Params:
        filter_ (:class:`ChatFilter`)
            The chat filter
        
        param_description (:class:`str`)
            Chat filter description
        
    """

    ID: str = Field("recommendedChatFilter", alias="@type")
    filter_: ChatFilter = Field(..., alias='filter')
    param_description: str

    @staticmethod
    def read(q: dict) -> RecommendedChatFilter:
        return RecommendedChatFilter.construct(**q)
