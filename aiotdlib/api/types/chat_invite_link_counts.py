# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_invite_link_count import ChatInviteLinkCount
from ..base_object import BaseObject


class ChatInviteLinkCounts(BaseObject):
    """
    Contains a list of chat invite link counts
    
    Params:
        invite_link_counts (:obj:`list[ChatInviteLinkCount]`)
            List of invite linkcounts
        
    """

    ID: str = Field("chatInviteLinkCounts", alias="@type")
    invite_link_counts: list[ChatInviteLinkCount]

    @staticmethod
    def read(q: dict) -> ChatInviteLinkCounts:
        return ChatInviteLinkCounts.construct(**q)
