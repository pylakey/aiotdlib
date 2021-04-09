# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message import Message
from ..base_object import BaseObject


class Messages(BaseObject):
    """
    Contains a list of messages
    
    Params:
        total_count (:class:`int`)
            Approximate total count of messages found
        
        messages (:obj:`list[Message]`)
            List of messages; messages may be null
        
    """

    ID: str = Field("messages", alias="@type")
    total_count: int
    messages: list[typing.Optional[Message]] = None

    @staticmethod
    def read(q: dict) -> Messages:
        return Messages.construct(**q)
