# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatInviteLink(BaseObject):
    """
    Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        invite_link (:class:`str`)
            Invite link to get
        
    """

    ID: str = Field("getChatInviteLink", alias="@type")
    chat_id: int
    invite_link: str

    @staticmethod
    def read(q: dict) -> GetChatInviteLink:
        return GetChatInviteLink.construct(**q)
