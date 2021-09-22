# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatMemberStatus
from ..types import MessageSender
from ..base_object import BaseObject


class SetChatMemberStatus(BaseObject):
    """
    Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for adding new members to the chat and transferring chat ownership; instead, use addChatMember or transferChatOwnership
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param member_id: Member identifier. Chats can be only banned and unbanned in supergroups and channels
    :type member_id: :class:`MessageSender`
    
    :param status: The new status of the member in the chat
    :type status: :class:`ChatMemberStatus`
    
    """

    ID: str = Field("setChatMemberStatus", alias="@type")
    chat_id: int
    member_id: MessageSender
    status: ChatMemberStatus

    @staticmethod
    def read(q: dict) -> SetChatMemberStatus:
        return SetChatMemberStatus.construct(**q)
