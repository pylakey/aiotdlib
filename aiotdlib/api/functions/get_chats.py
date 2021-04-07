# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatList


class GetChats(BaseObject):
    """
    Returns an ordered list of chats in a chat list. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. (For example, to get a list of chats from the beginning, the offset_order should be equal to a biggest signed 64-bit number 9223372036854775807 == 2^63 - 1). For optimal performance the number of returned chats is chosen by the library
    
    Params:
        chat_list (:class:`ChatList`)
            The chat list in which to return chats
        
        offset_order (:class:`int`)
            Chat order to return chats from
        
        offset_chat_id (:class:`int`)
            Chat identifier to return chats from
        
        limit (:class:`int`)
            The maximum number of chats to be returned. It is possible that fewer chats than the limit are returned even if the end of the list is not reached
        
    """

    ID: str = Field("getChats", alias="@type")
    chat_list: ChatList
    offset_order: int
    offset_chat_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetChats:
        return GetChats.construct(**q)
