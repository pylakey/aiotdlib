# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSchedulingState


class EditMessageSchedulingState(BaseObject):
    """
    Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed
    
    Params:
        chat_id (:class:`int`)
            The chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message
        
        scheduling_state (:class:`MessageSchedulingState`)
            The new message scheduling state. Pass null to send the message immediately
        
    """

    ID: str = Field("editMessageSchedulingState", alias="@type")
    chat_id: int
    message_id: int
    scheduling_state: MessageSchedulingState

    @staticmethod
    def read(q: dict) -> EditMessageSchedulingState:
        return EditMessageSchedulingState.construct(**q)
