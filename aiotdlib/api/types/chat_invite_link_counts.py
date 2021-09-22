# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_invite_link_count import ChatInviteLinkCount
from ..base_object import BaseObject


class ChatInviteLinkCounts(BaseObject):
    """
    Contains a list of chat invite link counts
    
    :param invite_link_counts: List of invite linkcounts
    :type invite_link_counts: :class:`list[ChatInviteLinkCount]`
    
    """

    ID: str = Field("chatInviteLinkCounts", alias="@type")
    invite_link_counts: list[ChatInviteLinkCount]

    @staticmethod
    def read(q: dict) -> ChatInviteLinkCounts:
        return ChatInviteLinkCounts.construct(**q)
