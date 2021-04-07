# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import TopChatCategory


class GetTopChats(BaseObject):
    """
    Returns a list of frequently used chats. Supported only if the chat info database is enabled
    
    Params:
        category (:class:`TopChatCategory`)
            Category of chats to be returned
        
        limit (:class:`int`)
            The maximum number of chats to be returned; up to 30
        
    """

    ID: str = Field("getTopChats", alias="@type")
    category: TopChatCategory
    limit: int

    @staticmethod
    def read(q: dict) -> GetTopChats:
        return GetTopChats.construct(**q)
