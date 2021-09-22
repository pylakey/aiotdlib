# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message_scheduling_state import MessageSchedulingState
from ..base_object import BaseObject


class MessageSendOptions(BaseObject):
    """
    Options to be used when a message is sent
    
    :param disable_notification: Pass true to disable notification for the message
    :type disable_notification: :class:`bool`
    
    :param from_background: Pass true if the message is sent from the background
    :type from_background: :class:`bool`
    
    :param scheduling_state: Message scheduling state. Messages sent to a secret chat, live location messages and self-destructing messages can't be scheduled
    :type scheduling_state: :class:`MessageSchedulingState`
    
    """

    ID: str = Field("messageSendOptions", alias="@type")
    disable_notification: bool
    from_background: bool
    scheduling_state: MessageSchedulingState

    @staticmethod
    def read(q: dict) -> MessageSendOptions:
        return MessageSendOptions.construct(**q)
