# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message import Message
from ..base_object import BaseObject


class FoundMessages(BaseObject):
    """
    Contains a list of messages found by a search
    
    :param total_count: Approximate total number of messages found; -1 if unknown
    :type total_count: :class:`int`
    
    :param messages: List of messages
    :type messages: :class:`list[Message]`
    
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`str`
    
    """

    ID: str = Field("foundMessages", alias="@type")
    total_count: int
    messages: list[Message]
    next_offset: str

    @staticmethod
    def read(q: dict) -> FoundMessages:
        return FoundMessages.construct(**q)
