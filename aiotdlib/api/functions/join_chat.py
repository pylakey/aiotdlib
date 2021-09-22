# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class JoinChat(BaseObject):
    """
    Adds the current user as a new member to a chat. Private and secret chats can't be joined using this method
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("joinChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> JoinChat:
        return JoinChat.construct(**q)
