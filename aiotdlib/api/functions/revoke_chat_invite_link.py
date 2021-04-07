# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RevokeChatInviteLink(BaseObject):
    """
    Revokes invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links. If a primary link is revoked, then additionally to the revoked link returns new primary link
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        invite_link (:class:`str`)
            Invite link to be revoked
        
    """

    ID: str = Field("revokeChatInviteLink", alias="@type")
    chat_id: int
    invite_link: str

    @staticmethod
    def read(q: dict) -> RevokeChatInviteLink:
        return RevokeChatInviteLink.construct(**q)
