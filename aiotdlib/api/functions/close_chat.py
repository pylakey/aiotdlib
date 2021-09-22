# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class CloseChat(BaseObject):
    """
    Informs TDLib that the chat is closed by the user. Many useful activities depend on the chat being opened or closed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("closeChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> CloseChat:
        return CloseChat.construct(**q)
