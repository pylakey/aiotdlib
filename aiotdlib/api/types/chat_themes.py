# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_theme import ChatTheme
from ..base_object import BaseObject


class ChatThemes(BaseObject):
    """
    Contains a list of chat themes
    
    Params:
        chat_themes (:obj:`list[ChatTheme]`)
            A list of chat themes
        
    """

    ID: str = Field("chatThemes", alias="@type")
    chat_themes: list[ChatTheme]

    @staticmethod
    def read(q: dict) -> ChatThemes:
        return ChatThemes.construct(**q)
