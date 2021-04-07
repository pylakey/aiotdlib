# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReplacePrimaryChatInviteLink(BaseObject):
    """
    Replaces current primary invite link for a chat with a new primary invite link. Available for basic groups, supergroups, and channels. Requires administrator privileges and can_invite_users right
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("replacePrimaryChatInviteLink", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> ReplacePrimaryChatInviteLink:
        return ReplacePrimaryChatInviteLink.construct(**q)
