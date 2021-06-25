# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_member_status import ChatMemberStatus
from .message_sender import MessageSender
from ..base_object import BaseObject


class ChatMember(BaseObject):
    """
    Information about a user or a chat as a member of another chat
    
    Params:
        member_id (:class:`MessageSender`)
            Identifier of the chat member. Currently, other chats can be only Left or Banned. Only supergroups and channels can have other chats as Left or Banned members and these chats must be supergroups or channels
        
        inviter_user_id (:class:`int`)
            Identifier of a user that invited/promoted/banned this member in the chat; 0 if unknown
        
        joined_chat_date (:class:`int`)
            Point in time (Unix timestamp) when the user joined the chat
        
        status (:class:`ChatMemberStatus`)
            Status of the member in the chat
        
    """

    ID: str = Field("chatMember", alias="@type")
    member_id: MessageSender
    inviter_user_id: int
    joined_chat_date: int
    status: ChatMemberStatus

    @staticmethod
    def read(q: dict) -> ChatMember:
        return ChatMember.construct(**q)
