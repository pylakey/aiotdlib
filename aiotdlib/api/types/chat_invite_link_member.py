# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatInviteLinkMember(BaseObject):
    """
    Describes a chat member joined a chat by an invite link
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        joined_chat_date (:class:`int`)
            Point in time (Unix timestamp) when the user joined the chat
        
    """

    ID: str = Field("chatInviteLinkMember", alias="@type")
    user_id: int
    joined_chat_date: int

    @staticmethod
    def read(q: dict) -> ChatInviteLinkMember:
        return ChatInviteLinkMember.construct(**q)
