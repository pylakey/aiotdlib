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
    
    Params:
        total_count (:class:`int`)
            Approximate total count of messages found; -1 if unknown
        
        messages (:obj:`list[Message]`)
            List of messages
        
        next_offset (:class:`str`)
            The offset for the next request. If empty, there are no more results
        
    """

    ID: str = Field("foundMessages", alias="@type")
    total_count: int
    messages: list[Message]
    next_offset: str

    @staticmethod
    def read(q: dict) -> FoundMessages:
        return FoundMessages.construct(**q)
