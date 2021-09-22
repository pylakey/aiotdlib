# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class MessageSendingState(BaseObject):
    """
    Contains information about the sending state of the message
    
    """

    ID: str = Field("messageSendingState", alias="@type")


class MessageSendingStateFailed(MessageSendingState):
    """
    The message failed to be sent
    
    :param error_code: An error code; 0 if unknown
    :type error_code: :class:`int`
    
    :param error_message: Error message
    :type error_message: :class:`str`
    
    :param can_retry: True, if the message can be re-sent
    :type can_retry: :class:`bool`
    
    :param retry_after: Time left before the message can be re-sent, in seconds. No update is sent when this field changes
    :type retry_after: :class:`float`
    
    """

    ID: str = Field("messageSendingStateFailed", alias="@type")
    error_code: int
    error_message: str
    can_retry: bool
    retry_after: float

    @staticmethod
    def read(q: dict) -> MessageSendingStateFailed:
        return MessageSendingStateFailed.construct(**q)


class MessageSendingStatePending(MessageSendingState):
    """
    The message is being sent now, but has not yet been delivered to the server
    
    """

    ID: str = Field("messageSendingStatePending", alias="@type")

    @staticmethod
    def read(q: dict) -> MessageSendingStatePending:
        return MessageSendingStatePending.construct(**q)
