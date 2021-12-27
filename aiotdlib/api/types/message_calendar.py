# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_calendar_day import MessageCalendarDay
from ..base_object import BaseObject


class MessageCalendar(BaseObject):
    """
    Contains information about found messages, split by days according to the option "utc_time_offset"
    
    :param total_count: Total number of found messages
    :type total_count: :class:`int`
    
    :param days: Information about messages sent
    :type days: :class:`list[MessageCalendarDay]`
    
    """

    ID: str = Field("messageCalendar", alias="@type")
    total_count: int
    days: list[MessageCalendarDay]

    @staticmethod
    def read(q: dict) -> MessageCalendar:
        return MessageCalendar.construct(**q)
