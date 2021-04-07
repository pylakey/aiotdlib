# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import TopChatCategory


class RemoveTopChat(BaseObject):
    """
    Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled
    
    Params:
        category (:class:`TopChatCategory`)
            Category of frequently used chats
        
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("removeTopChat", alias="@type")
    category: TopChatCategory
    chat_id: int

    @staticmethod
    def read(q: dict) -> RemoveTopChat:
        return RemoveTopChat.construct(**q)
