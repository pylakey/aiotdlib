# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_scheduling_state import MessageSchedulingState
from ..base_object import BaseObject


class MessageSendOptions(BaseObject):
    """
    Options to be used when a message is sent
    
    Params:
        disable_notification (:class:`bool`)
            Pass true to disable notification for the message
        
        from_background (:class:`bool`)
            Pass true if the message is sent from the background
        
        scheduling_state (:class:`MessageSchedulingState`)
            Message scheduling state. Messages sent to a secret chat, live location messages and self-destructing messages can't be scheduled
        
    """

    ID: str = Field("messageSendOptions", alias="@type")
    disable_notification: bool
    from_background: bool
    scheduling_state: MessageSchedulingState

    @staticmethod
    def read(q: dict) -> MessageSendOptions:
        return MessageSendOptions.construct(**q)
