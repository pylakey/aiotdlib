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
    
    :param total_count: Approximate total count of messages found
    :type total_count: :class:`int`
    
    :param messages: List of messages; messages may be null, defaults to None
    :type messages: :class:`list[Message]`, optional
    
    """

    ID: str = Field("messages", alias="@type")
    total_count: int
    messages: list[typing.Optional[Message]] = None

    @staticmethod
    def read(q: dict) -> Messages:
        return Messages.construct(**q)
