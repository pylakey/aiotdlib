# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatFilterInfo(BaseObject):
    """
    Contains basic information about a chat filter
    
    :param id: Unique chat filter identifier
    :type id: :class:`int`
    
    :param title: The title of the filter; 1-12 characters without line feeds
    :type title: :class:`str`
    
    :param icon_name: The icon name for short filter representation. One of "All", "Unread", "Unmuted", "Bots", "Channels", "Groups", "Private", "Custom", "Setup", "Cat", "Crown", "Favorite", "Flower", "Game", "Home", "Love", "Mask", "Party", "Sport", "Study", "Trade", "Travel", "Work"
    :type icon_name: :class:`str`
    
    """

    ID: str = Field("chatFilterInfo", alias="@type")
    id: int
    title: str = Field(..., min_length=1, max_length=12)
    icon_name: str

    @staticmethod
    def read(q: dict) -> ChatFilterInfo:
        return ChatFilterInfo.construct(**q)
