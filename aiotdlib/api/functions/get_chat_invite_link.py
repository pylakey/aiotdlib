# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatInviteLink(BaseObject):
    """
    Returns information about an invite link. Requires administrator privileges and can_invite_users right in the chat to get own links and owner privileges to get other links
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param invite_link: Invite link to get
    :type invite_link: :class:`str`
    
    """

    ID: str = Field("getChatInviteLink", alias="@type")
    chat_id: int
    invite_link: str

    @staticmethod
    def read(q: dict) -> GetChatInviteLink:
        return GetChatInviteLink.construct(**q)
