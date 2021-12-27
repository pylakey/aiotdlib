# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message import Message
from ..base_object import BaseObject


class MessageCalendarDay(BaseObject):
    """
    Contains information about found messages sent on a specific day
    
    :param total_count: Total number of found messages sent on the day
    :type total_count: :class:`int`
    
    :param message: First message sent on the day
    :type message: :class:`Message`
    
    """

    ID: str = Field("messageCalendarDay", alias="@type")
    total_count: int
    message: Message

    @staticmethod
    def read(q: dict) -> MessageCalendarDay:
        return MessageCalendarDay.construct(**q)
