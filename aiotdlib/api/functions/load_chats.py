# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatList
from ..base_object import BaseObject


class LoadChats(BaseObject):
    """
    Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats has been loaded
    
    :param chat_list: The chat list in which to load chats
    :type chat_list: :class:`ChatList`
    
    :param limit: The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
    :type limit: :class:`int`
    
    """

    ID: str = Field("loadChats", alias="@type")
    chat_list: ChatList
    limit: int

    @staticmethod
    def read(q: dict) -> LoadChats:
        return LoadChats.construct(**q)
