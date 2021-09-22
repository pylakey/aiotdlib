# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CheckChatInviteLink(BaseObject):
    """
    Checks the validity of an invite link for a chat and returns information about the corresponding chat
    
    :param invite_link: Invite link to be checked
    :type invite_link: :class:`str`
    
    """

    ID: str = Field("checkChatInviteLink", alias="@type")
    invite_link: str

    @staticmethod
    def read(q: dict) -> CheckChatInviteLink:
        return CheckChatInviteLink.construct(**q)
