# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatInviteLink(BaseObject):
    """
    Contains a chat invite link
    
    Params:
        invite_link (:class:`str`)
            Chat invite link
        
        creator_user_id (:class:`int`)
            User identifier of an administrator created the link
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the link was created
        
        edit_date (:class:`int`)
            Point in time (Unix timestamp) when the link was last edited; 0 if never or unknown
        
        expire_date (:class:`int`)
            Point in time (Unix timestamp) when the link will expire; 0 if never
        
        member_limit (:class:`int`)
            Maximum number of members, which can join the chat using the link simultaneously; 0 if not limited
        
        member_count (:class:`int`)
            Number of chat members, which joined the chat using the link
        
        is_primary (:class:`bool`)
            True, if the link is primary. Primary invite link can't have expire date or usage limit. There is exactly one primary invite link for each administrator with can_invite_users right at a given time
        
        is_revoked (:class:`bool`)
            True, if the link was revoked
        
    """

    ID: str = Field("chatInviteLink", alias="@type")
    invite_link: str
    creator_user_id: int
    date: int
    edit_date: int
    expire_date: int
    member_limit: int
    member_count: int
    is_primary: bool
    is_revoked: bool

    @staticmethod
    def read(q: dict) -> ChatInviteLink:
        return ChatInviteLink.construct(**q)
