# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatInviteLinks(BaseObject):
    """
    Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        creator_user_id (:class:`int`)
            User identifier of a chat administrator. Must be an identifier of the current user for non-owner
        
        is_revoked (:class:`bool`)
            Pass true if revoked links needs to be returned instead of active or expired
        
        offset_date (:class:`int`)
            Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
        
        offset_invite_link (:class:`str`)
            Invite link starting after which to return invite links; use empty string to get results from the beginning
        
        limit (:class:`int`)
            The maximum number of invite links to return
        
    """

    ID: str = Field("getChatInviteLinks", alias="@type")
    chat_id: int
    creator_user_id: int
    is_revoked: bool
    offset_date: int
    offset_invite_link: str
    limit: int

    @staticmethod
    def read(q: dict) -> GetChatInviteLinks:
        return GetChatInviteLinks.construct(**q)
