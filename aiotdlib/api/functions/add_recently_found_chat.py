# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AddRecentlyFoundChat(BaseObject):
    """
    Adds a chat to the list of recently found chats. The chat is added to the beginning of the list. If the chat is already in the list, it will be removed from the list first
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to add
        
    """

    ID: str = Field("addRecentlyFoundChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> AddRecentlyFoundChat:
        return AddRecentlyFoundChat.construct(**q)
