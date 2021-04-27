# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class GetChatMember(BaseObject):
    """
    Returns information about a single member of a chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        member_id (:class:`MessageSender`)
            Member identifier
        
    """

    ID: str = Field("getChatMember", alias="@type")
    chat_id: int
    member_id: MessageSender

    @staticmethod
    def read(q: dict) -> GetChatMember:
        return GetChatMember.construct(**q)
