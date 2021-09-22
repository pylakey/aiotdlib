# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import MessageSchedulingState
from ..base_object import BaseObject


class EditMessageSchedulingState(BaseObject):
    """
    Edits the time when a scheduled message will be sent. Scheduling state of all messages in the same album or forwarded together with the message will be also changed
    
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param scheduling_state: The new message scheduling state. Pass null to send the message immediately
    :type scheduling_state: :class:`MessageSchedulingState`
    
    """

    ID: str = Field("editMessageSchedulingState", alias="@type")
    chat_id: int
    message_id: int
    scheduling_state: MessageSchedulingState

    @staticmethod
    def read(q: dict) -> EditMessageSchedulingState:
        return EditMessageSchedulingState.construct(**q)
