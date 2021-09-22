# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CreateChatInviteLink(BaseObject):
    """
    Creates a new invite link for a chat. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right in the chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param expire_date: Point in time (Unix timestamp) when the link will expire; pass 0 if never
    :type expire_date: :class:`int`
    
    :param member_limit: The maximum number of chat members that can join the chat by the link simultaneously; 0-99999; pass 0 if not limited
    :type member_limit: :class:`int`
    
    """

    ID: str = Field("createChatInviteLink", alias="@type")
    chat_id: int
    expire_date: int
    member_limit: int

    @staticmethod
    def read(q: dict) -> CreateChatInviteLink:
        return CreateChatInviteLink.construct(**q)
