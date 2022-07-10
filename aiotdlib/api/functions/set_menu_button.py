# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BotMenuButton


class SetMenuButton(BaseObject):
    """
    Sets menu button for the given user or for all users; for bots only
    
    :param user_id: Identifier of the user or 0 to set menu button for all users
    :type user_id: :class:`int`
    
    :param menu_button: New menu button
    :type menu_button: :class:`BotMenuButton`
    
    """

    ID: str = Field("setMenuButton", alias="@type")
    user_id: int
    menu_button: BotMenuButton

    @staticmethod
    def read(q: dict) -> SetMenuButton:
        return SetMenuButton.construct(**q)
