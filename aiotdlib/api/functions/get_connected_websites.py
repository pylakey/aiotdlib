# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetConnectedWebsites(BaseObject):
    """
    Returns all website where the current user used Telegram to log in
    
    """

    ID: str = Field("getConnectedWebsites", alias="@type")

    @staticmethod
    def read(q: dict) -> GetConnectedWebsites:
        return GetConnectedWebsites.construct(**q)
