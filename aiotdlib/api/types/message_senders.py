# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_sender import MessageSender
from ..base_object import BaseObject


class MessageSenders(BaseObject):
    """
    Represents a list of message senders
    
    Params:
        total_count (:class:`int`)
            Approximate total count of messages senders found
        
        senders (:obj:`list[MessageSender]`)
            List of message senders
        
    """

    ID: str = Field("messageSenders", alias="@type")
    total_count: int
    senders: list[MessageSender]

    @staticmethod
    def read(q: dict) -> MessageSenders:
        return MessageSenders.construct(**q)
