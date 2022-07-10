# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class BotMenuButton(BaseObject):
    """
    Describes a button to be shown instead of bot commands menu button
    
    :param text: Text of the button
    :type text: :class:`str`
    
    :param url: URL to be passed to openWebApp
    :type url: :class:`str`
    
    """

    ID: str = Field("botMenuButton", alias="@type")
    text: str
    url: str

    @staticmethod
    def read(q: dict) -> BotMenuButton:
        return BotMenuButton.construct(**q)
