# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_invite_link_member import ChatInviteLinkMember
from ..base_object import BaseObject


class ChatInviteLinkMembers(BaseObject):
    """
    Contains a list of chat members joined a chat by an invite link
    
    Params:
        total_count (:class:`int`)
            Approximate total count of chat members found
        
        members (:obj:`list[ChatInviteLinkMember]`)
            List of chat members, joined a chat by an invite link
        
    """

    ID: str = Field("chatInviteLinkMembers", alias="@type")
    total_count: int
    members: list[ChatInviteLinkMember]

    @staticmethod
    def read(q: dict) -> ChatInviteLinkMembers:
        return ChatInviteLinkMembers.construct(**q)
