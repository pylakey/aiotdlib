# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckChatUsername(BaseObject):
    """
    Checks whether a username can be set for a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier; should be identifier of a supergroup chat, or a channel chat, or a private chat with self, or zero if the chat is being created
        
        username (:class:`str`)
            Username to be checked
        
    """

    ID: str = Field("checkChatUsername", alias="@type")
    chat_id: int
    username: str

    @staticmethod
    def read(q: dict) -> CheckChatUsername:
        return CheckChatUsername.construct(**q)
