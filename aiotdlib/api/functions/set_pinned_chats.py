# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatList


class SetPinnedChats(BaseObject):
    """
    Changes the order of pinned chats
    
    Params:
        chat_list (:class:`ChatList`)
            Chat list in which to change the order of pinned chats
        
        chat_ids (:obj:`list[int]`)
            The new list of pinned chats
        
    """

    ID: str = Field("setPinnedChats", alias="@type")
    chat_list: ChatList
    chat_ids: list[int]

    @staticmethod
    def read(q: dict) -> SetPinnedChats:
        return SetPinnedChats.construct(**q)
