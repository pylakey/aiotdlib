# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import TopChatCategory
from ..base_object import BaseObject


class RemoveTopChat(BaseObject):
    """
    Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled
    
    :param category: Category of frequently used chats
    :type category: :class:`TopChatCategory`
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("removeTopChat", alias="@type")
    category: TopChatCategory
    chat_id: int

    @staticmethod
    def read(q: dict) -> RemoveTopChat:
        return RemoveTopChat.construct(**q)
