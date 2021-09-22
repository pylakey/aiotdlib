# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatInviteLinks(BaseObject):
    """
    Returns invite links for a chat created by specified administrator. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param creator_user_id: User identifier of a chat administrator. Must be an identifier of the current user for non-owner
    :type creator_user_id: :class:`int`
    
    :param is_revoked: Pass true if revoked links needs to be returned instead of active or expired
    :type is_revoked: :class:`bool`
    
    :param offset_date: Creation date of an invite link starting after which to return invite links; use 0 to get results from the beginning
    :type offset_date: :class:`int`
    
    :param offset_invite_link: Invite link starting after which to return invite links; use empty string to get results from the beginning
    :type offset_invite_link: :class:`str`
    
    :param limit: The maximum number of invite links to return
    :type limit: :class:`int`
    
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
