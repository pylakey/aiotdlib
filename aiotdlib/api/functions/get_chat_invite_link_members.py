# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatInviteLinkMember


class GetChatInviteLinkMembers(BaseObject):
    """
    Returns chat members joined a chat by an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        invite_link (:class:`str`)
            Invite link for which to return chat members
        
        offset_member (:class:`ChatInviteLinkMember`)
            A chat member from which to return next chat members; use null to get results from the beginning
        
        limit (:class:`int`)
            Maximum number of chat members to return
        
    """

    ID: str = Field("getChatInviteLinkMembers", alias="@type")
    chat_id: int
    invite_link: str
    offset_member: ChatInviteLinkMember
    limit: int

    @staticmethod
    def read(q: dict) -> GetChatInviteLinkMembers:
        return GetChatInviteLinkMembers.construct(**q)
