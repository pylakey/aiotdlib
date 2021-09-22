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


class GetChats(BaseObject):
    """
    Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats instead to maintain chat lists
    
    :param chat_list: The chat list in which to return chats
    :type chat_list: :class:`ChatList`
    
    :param limit: The maximum number of chats to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("getChats", alias="@type")
    chat_list: ChatList
    limit: int

    @staticmethod
    def read(q: dict) -> GetChats:
        return GetChats.construct(**q)
