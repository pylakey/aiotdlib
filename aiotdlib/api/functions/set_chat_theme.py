# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetChatTheme(BaseObject):
    """
    Changes the chat theme. Supported only in private and secret chats
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param theme_name: Name of the new chat theme; may be empty to return the default theme
    :type theme_name: :class:`str`
    
    """

    ID: str = Field("setChatTheme", alias="@type")
    chat_id: int
    theme_name: str

    @staticmethod
    def read(q: dict) -> SetChatTheme:
        return SetChatTheme.construct(**q)
