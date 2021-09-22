# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatListsToAddChat(BaseObject):
    """
    Returns chat lists to which the chat can be added. This is an offline request
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChatListsToAddChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatListsToAddChat:
        return GetChatListsToAddChat.construct(**q)
