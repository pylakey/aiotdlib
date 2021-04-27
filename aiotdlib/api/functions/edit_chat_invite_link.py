# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class EditChatInviteLink(BaseObject):
    """
    Edits a non-primary invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat for own links and owner privileges for other links
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        invite_link (:class:`str`)
            Invite link to be edited
        
        expire_date (:class:`int`)
            Point in time (Unix timestamp) when the link will expire; pass 0 if never
        
        member_limit (:class:`int`)
            The maximum number of chat members that can join the chat by the link simultaneously; 0-99999; pass 0 if not limited
        
    """

    ID: str = Field("editChatInviteLink", alias="@type")
    chat_id: int
    invite_link: str
    expire_date: int
    member_limit: int

    @staticmethod
    def read(q: dict) -> EditChatInviteLink:
        return EditChatInviteLink.construct(**q)
