# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CheckChatUsername(BaseObject):
    """
    Checks whether a username can be set for a chat
    
    :param chat_id: Chat identifier; should be identifier of a supergroup chat, or a channel chat, or a private chat with self, or zero if the chat is being created
    :type chat_id: :class:`int`
    
    :param username: Username to be checked
    :type username: :class:`str`
    
    """

    ID: str = Field("checkChatUsername", alias="@type")
    chat_id: int
    username: str

    @staticmethod
    def read(q: dict) -> CheckChatUsername:
        return CheckChatUsername.construct(**q)
