# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReadAllChatReactions(BaseObject):
    """
    Marks all reactions in a chat as read
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("readAllChatReactions", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> ReadAllChatReactions:
        return ReadAllChatReactions.construct(**q)
