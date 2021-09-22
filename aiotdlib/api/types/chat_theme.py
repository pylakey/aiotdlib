# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .theme_settings import ThemeSettings
from ..base_object import BaseObject


class ChatTheme(BaseObject):
    """
    Describes a chat theme
    
    :param name: Theme name
    :type name: :class:`str`
    
    :param light_settings: Theme settings for a light chat theme
    :type light_settings: :class:`ThemeSettings`
    
    :param dark_settings: Theme settings for a dark chat theme
    :type dark_settings: :class:`ThemeSettings`
    
    """

    ID: str = Field("chatTheme", alias="@type")
    name: str
    light_settings: ThemeSettings
    dark_settings: ThemeSettings

    @staticmethod
    def read(q: dict) -> ChatTheme:
        return ChatTheme.construct(**q)
