# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMenuButton(BaseObject):
    """
    Returns menu button set by the bot for the given user; for bots only
    
    :param user_id: Identifier of the user or 0 to get the default menu button
    :type user_id: :class:`int`
    
    """

    ID: str = Field("getMenuButton", alias="@type")
    user_id: int

    @staticmethod
    def read(q: dict) -> GetMenuButton:
        return GetMenuButton.construct(**q)
