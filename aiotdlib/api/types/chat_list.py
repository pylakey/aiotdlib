# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatList(BaseObject):
    """
    Describes a list of chats
    
    """

    ID: str = Field("chatList", alias="@type")


class ChatListArchive(ChatList):
    """
    A list of chats usually located at the top of the main chat list. Unmuted chats are automatically moved from the Archive to the Main chat list when a new message arrives
    
    """

    ID: str = Field("chatListArchive", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatListArchive:
        return ChatListArchive.construct(**q)


class ChatListFilter(ChatList):
    """
    A list of chats belonging to a chat filter
    
    Params:
        chat_filter_id (:class:`int`)
            Chat filter identifier
        
    """

    ID: str = Field("chatListFilter", alias="@type")
    chat_filter_id: int

    @staticmethod
    def read(q: dict) -> ChatListFilter:
        return ChatListFilter.construct(**q)


class ChatListMain(ChatList):
    """
    A main list of chats
    
    """

    ID: str = Field("chatListMain", alias="@type")

    @staticmethod
    def read(q: dict) -> ChatListMain:
        return ChatListMain.construct(**q)
