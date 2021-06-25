# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatMemberStatus
from ..types import MessageSender


class SetChatMemberStatus(BaseObject):
    """
    Changes the status of a chat member, needs appropriate privileges. This function is currently not suitable for adding new members to the chat and transferring chat ownership; instead, use addChatMember or transferChatOwnership
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        member_id (:class:`MessageSender`)
            Member identifier. Chats can be only banned and unbanned in supergroups and channels
        
        status (:class:`ChatMemberStatus`)
            The new status of the member in the chat
        
    """

    ID: str = Field("setChatMemberStatus", alias="@type")
    chat_id: int
    member_id: MessageSender
    status: ChatMemberStatus

    @staticmethod
    def read(q: dict) -> SetChatMemberStatus:
        return SetChatMemberStatus.construct(**q)
