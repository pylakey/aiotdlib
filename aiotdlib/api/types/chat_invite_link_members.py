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
    Contains a list of chat members joined a chat via an invite link
    
    :param total_count: Approximate total number of chat members found
    :type total_count: :class:`int`
    
    :param members: List of chat members, joined a chat via an invite link
    :type members: :class:`list[ChatInviteLinkMember]`
    
    """

    ID: str = Field("chatInviteLinkMembers", alias="@type")
    total_count: int
    members: list[ChatInviteLinkMember]

    @staticmethod
    def read(q: dict) -> ChatInviteLinkMembers:
        return ChatInviteLinkMembers.construct(**q)
