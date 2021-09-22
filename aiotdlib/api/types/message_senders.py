# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class MessageSenders(BaseObject):
    """
    Represents a list of message senders
    
    :param total_count: Approximate total count of messages senders found
    :type total_count: :class:`int`
    
    :param senders: List of message senders
    :type senders: :class:`list[MessageSender]`
    
    """

    ID: str = Field("messageSenders", alias="@type")
    total_count: int
    senders: list[MessageSender]

    @staticmethod
    def read(q: dict) -> MessageSenders:
        return MessageSenders.construct(**q)
