# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .theme_settings import ThemeSettings
from ..base_object import BaseObject


class ChatTheme(BaseObject):
    """
    Describes a chat theme
    
    Params:
        name (:class:`str`)
            Theme name
        
        light_settings (:class:`ThemeSettings`)
            Theme settings for a light chat theme
        
        dark_settings (:class:`ThemeSettings`)
            Theme settings for a dark chat theme
        
    """

    ID: str = Field("chatTheme", alias="@type")
    name: str
    light_settings: ThemeSettings
    dark_settings: ThemeSettings

    @staticmethod
    def read(q: dict) -> ChatTheme:
        return ChatTheme.construct(**q)
