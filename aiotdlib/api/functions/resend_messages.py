# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ResendMessages(BaseObject):
    """
    Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message
    
    :param chat_id: Identifier of the chat to send messages
    :type chat_id: :class:`int`
    
    :param message_ids: Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order
    :type message_ids: :class:`list[int]`
    
    """

    ID: str = Field("resendMessages", alias="@type")
    chat_id: int
    message_ids: list[int]

    @staticmethod
    def read(q: dict) -> ResendMessages:
        return ResendMessages.construct(**q)
