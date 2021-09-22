# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class Chats(BaseObject):
    """
    Represents a list of chats
    
    :param total_count: Approximate total count of chats found
    :type total_count: :class:`int`
    
    :param chat_ids: List of chat identifiers
    :type chat_ids: :class:`list[int]`
    
    """

    ID: str = Field("chats", alias="@type")
    total_count: int
    chat_ids: list[int]

    @staticmethod
    def read(q: dict) -> Chats:
        return Chats.construct(**q)
