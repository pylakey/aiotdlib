# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ReadAllChatMentions(BaseObject):
    """
    Marks all mentions in a chat as read
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("readAllChatMentions", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> ReadAllChatMentions:
        return ReadAllChatMentions.construct(**q)
