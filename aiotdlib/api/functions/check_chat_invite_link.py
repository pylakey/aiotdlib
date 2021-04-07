# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckChatInviteLink(BaseObject):
    """
    Checks the validity of an invite link for a chat and returns information about the corresponding chat
    
    Params:
        invite_link (:class:`str`)
            Invite link to be checked; must have URL "t.me", "telegram.me", or "telegram.dog" and query beginning with "/joinchat/" or "/+"
        
    """

    ID: str = Field("checkChatInviteLink", alias="@type")
    invite_link: str

    @staticmethod
    def read(q: dict) -> CheckChatInviteLink:
        return CheckChatInviteLink.construct(**q)
