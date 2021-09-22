# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_filter import ChatFilter
from ..base_object import BaseObject


class RecommendedChatFilter(BaseObject):
    """
    Describes a recommended chat filter
    
    :param filter_: The chat filter
    :type filter_: :class:`ChatFilter`
    
    :param param_description: Chat filter description
    :type param_description: :class:`str`
    
    """

    ID: str = Field("recommendedChatFilter", alias="@type")
    filter_: ChatFilter = Field(..., alias='filter')
    param_description: str

    @staticmethod
    def read(q: dict) -> RecommendedChatFilter:
        return RecommendedChatFilter.construct(**q)
