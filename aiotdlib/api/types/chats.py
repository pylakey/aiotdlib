# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class Chats(BaseObject):
    """
    Represents a list of chats
    
    Params:
        total_count (:class:`int`)
            Approximate total count of chats found
        
        chat_ids (:obj:`list[int]`)
            List of chat identifiers
        
    """

    ID: str = Field("chats", alias="@type")
    total_count: int
    chat_ids: list[int]

    @staticmethod
    def read(q: dict) -> Chats:
        return Chats.construct(**q)
