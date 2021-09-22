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


class SetPinnedChats(BaseObject):
    """
    Changes the order of pinned chats
    
    :param chat_list: Chat list in which to change the order of pinned chats
    :type chat_list: :class:`ChatList`
    
    :param chat_ids: The new list of pinned chats
    :type chat_ids: :class:`list[int]`
    
    """

    ID: str = Field("setPinnedChats", alias="@type")
    chat_list: ChatList
    chat_ids: list[int]

    @staticmethod
    def read(q: dict) -> SetPinnedChats:
        return SetPinnedChats.construct(**q)
