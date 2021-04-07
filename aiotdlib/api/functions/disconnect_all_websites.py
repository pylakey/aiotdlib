# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class DisconnectAllWebsites(BaseObject):
    """
    Disconnects all websites from the current user's Telegram account
    
    """

    ID: str = Field("disconnectAllWebsites", alias="@type")

    @staticmethod
    def read(q: dict) -> DisconnectAllWebsites:
        return DisconnectAllWebsites.construct(**q)
