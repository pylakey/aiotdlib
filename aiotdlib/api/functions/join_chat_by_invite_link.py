# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class JoinChatByInviteLink(BaseObject):
    """
    Uses an invite link to add the current user to the chat if possible
    
    :param invite_link: Invite link to use
    :type invite_link: :class:`str`
    
    """

    ID: str = Field("joinChatByInviteLink", alias="@type")
    invite_link: str

    @staticmethod
    def read(q: dict) -> JoinChatByInviteLink:
        return JoinChatByInviteLink.construct(**q)
