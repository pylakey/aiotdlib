# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_member_status import ChatMemberStatus
from .message_sender import MessageSender
from ..base_object import BaseObject


class ChatMember(BaseObject):
    """
    Information about a user or a chat as a member of another chat
    
    :param member_id: Identifier of the chat member. Currently, other chats can be only Left or Banned. Only supergroups and channels can have other chats as Left or Banned members and these chats must be supergroups or channels
    :type member_id: :class:`MessageSender`
    
    :param inviter_user_id: Identifier of a user that invited/promoted/banned this member in the chat; 0 if unknown
    :type inviter_user_id: :class:`int`
    
    :param joined_chat_date: Point in time (Unix timestamp) when the user joined the chat
    :type joined_chat_date: :class:`int`
    
    :param status: Status of the member in the chat
    :type status: :class:`ChatMemberStatus`
    
    """

    ID: str = Field("chatMember", alias="@type")
    member_id: MessageSender
    inviter_user_id: int
    joined_chat_date: int
    status: ChatMemberStatus

    @staticmethod
    def read(q: dict) -> ChatMember:
        return ChatMember.construct(**q)
