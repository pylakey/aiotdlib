# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatMember(BaseObject):
    """
    Returns information about a single member of a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        user_id (:class:`int`)
            User identifier
        
    """

    ID: str = Field("getChatMember", alias="@type")
    chat_id: int
    user_id: int

    @staticmethod
    def read(q: dict) -> GetChatMember:
        return GetChatMember.construct(**q)
