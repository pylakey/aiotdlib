# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class RemoveRecentlyFoundChat(BaseObject):
    """
    Removes a chat from the list of recently found chats
    
    :param chat_id: Identifier of the chat to be removed
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("removeRecentlyFoundChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> RemoveRecentlyFoundChat:
        return RemoveRecentlyFoundChat.construct(**q)
