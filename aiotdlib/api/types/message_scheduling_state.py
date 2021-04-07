# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class MessageSchedulingState(BaseObject):
    """
    Contains information about the time when a scheduled message will be sent
    
    """

    ID: str = Field("messageSchedulingState", alias="@type")


class MessageSchedulingStateSendAtDate(MessageSchedulingState):
    """
    The message will be sent at the specified date
    
    Params:
        send_date (:class:`int`)
            Date the message will be sent. The date must be within 367 days in the future
        
    """

    ID: str = Field("messageSchedulingStateSendAtDate", alias="@type")
    send_date: int

    @staticmethod
    def read(q: dict) -> MessageSchedulingStateSendAtDate:
        return MessageSchedulingStateSendAtDate.construct(**q)


class MessageSchedulingStateSendWhenOnline(MessageSchedulingState):
    """
    The message will be sent when the peer will be online. Applicable to private chats only and when the exact online status of the peer is known
    
    """

    ID: str = Field("messageSchedulingStateSendWhenOnline", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageSchedulingStateSendWhenOnline:
        return MessageSchedulingStateSendWhenOnline.construct(**q)
