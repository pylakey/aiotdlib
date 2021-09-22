# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatInviteLinkMember
from ..base_object import BaseObject


class GetChatInviteLinkMembers(BaseObject):
    """
    Returns chat members joined a chat by an invite link. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param invite_link: Invite link for which to return chat members
    :type invite_link: :class:`str`
    
    :param offset_member: A chat member from which to return next chat members; use null to get results from the beginning
    :type offset_member: :class:`ChatInviteLinkMember`
    
    :param limit: The maximum number of chat members to return
    :type limit: :class:`int`
    
    """

    ID: str = Field("getChatInviteLinkMembers", alias="@type")
    chat_id: int
    invite_link: str
    offset_member: ChatInviteLinkMember
    limit: int

    @staticmethod
    def read(q: dict) -> GetChatInviteLinkMembers:
        return GetChatInviteLinkMembers.construct(**q)
