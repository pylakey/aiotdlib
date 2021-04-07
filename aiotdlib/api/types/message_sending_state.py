# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

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
    
    Params:
        error_code (:class:`int`)
            An error code; 0 if unknown
        
        error_message (:class:`str`)
            Error message
        
        can_retry (:class:`bool`)
            True, if the message can be re-sent
        
        retry_after (:class:`float`)
            Time left before the message can be re-sent, in seconds. No update is sent when this field changes
        
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
