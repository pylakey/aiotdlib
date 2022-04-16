# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_invite_link import ChatInviteLink
from ..base_object import BaseObject


class ChatInviteLinks(BaseObject):
    """
    Contains a list of chat invite links
    
    :param total_count: Approximate total number of chat invite links found
    :type total_count: :class:`int`
    
    :param invite_links: List of invite links
    :type invite_links: :class:`list[ChatInviteLink]`
    
    """

    ID: str = Field("chatInviteLinks", alias="@type")
    total_count: int
    invite_links: list[ChatInviteLink]

    @staticmethod
    def read(q: dict) -> ChatInviteLinks:
        return ChatInviteLinks.construct(**q)
