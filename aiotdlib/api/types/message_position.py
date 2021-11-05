# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class MessagePosition(BaseObject):
    """
    Contains information about a message in a specific position
    
    :param position: 0-based message position in the full list of suitable messages
    :type position: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the message was sent
    :type date: :class:`int`
    
    """

    ID: str = Field("messagePosition", alias="@type")
    position: int
    message_id: int
    date: int

    @staticmethod
    def read(q: dict) -> MessagePosition:
        return MessagePosition.construct(**q)
