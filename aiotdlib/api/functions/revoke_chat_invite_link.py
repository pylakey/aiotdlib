# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RevokeChatInviteLink(BaseObject):
    """
    Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links. If a primary link is revoked, then additionally to the revoked link returns new primary link
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param invite_link: Invite link to be revoked
    :type invite_link: :class:`str`
    
    """

    ID: str = Field("revokeChatInviteLink", alias="@type")
    chat_id: int
    invite_link: str

    @staticmethod
    def read(q: dict) -> RevokeChatInviteLink:
        return RevokeChatInviteLink.construct(**q)
