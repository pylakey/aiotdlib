# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetChatTheme(BaseObject):
    """
    Changes the chat theme. Supported only in private and secret chats
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        theme_name (:class:`str`)
            Name of the new chat theme; may be empty to return the default theme
        
    """

    ID: str = Field("setChatTheme", alias="@type")
    chat_id: int
    theme_name: str

    @staticmethod
    def read(q: dict) -> SetChatTheme:
        return SetChatTheme.construct(**q)
