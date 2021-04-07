# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetInviteText(BaseObject):
    """
    Returns the default text for invitation messages to be used as a placeholder when the current user invites friends to Telegram
    
    """

    ID: str = Field("getInviteText", alias="@type")

    @staticmethod
    def read(q: dict) -> GetInviteText:
        return GetInviteText.construct(**q)
