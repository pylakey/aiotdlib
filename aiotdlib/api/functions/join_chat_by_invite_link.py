# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class JoinChatByInviteLink(BaseObject):
    """
    Uses an invite link to add the current user to the chat if possible
    
    Params:
        invite_link (:class:`str`)
            Invite link to use
        
    """

    ID: str = Field("joinChatByInviteLink", alias="@type")
    invite_link: str

    @staticmethod
    def read(q: dict) -> JoinChatByInviteLink:
        return JoinChatByInviteLink.construct(**q)
