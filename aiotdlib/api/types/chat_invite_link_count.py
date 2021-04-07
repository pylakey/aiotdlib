# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatInviteLinkCount(BaseObject):
    """
    Describes a chat administrator with a number of active and revoked chat invite links
    
    Params:
        user_id (:class:`int`)
            Administrator's user identifier
        
        invite_link_count (:class:`int`)
            Number of active invite links
        
        revoked_invite_link_count (:class:`int`)
            Number of revoked invite links
        
    """

    ID: str = Field("chatInviteLinkCount", alias="@type")
    user_id: int
    invite_link_count: int
    revoked_invite_link_count: int

    @staticmethod
    def read(q: dict) -> ChatInviteLinkCount:
        return ChatInviteLinkCount.construct(**q)
