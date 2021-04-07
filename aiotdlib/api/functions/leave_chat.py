# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LeaveChat(BaseObject):
    """
    Removes the current user from chat members. Private and secret chats can't be left using this method
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("leaveChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> LeaveChat:
        return LeaveChat.construct(**q)
