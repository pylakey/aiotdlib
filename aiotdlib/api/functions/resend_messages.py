# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResendMessages(BaseObject):
    """
    Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message

    :param chat_id: Identifier of the chat to send messages
    :type chat_id: :class:`Int53`
    :param message_ids: Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order
    :type message_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["resendMessages"] = "resendMessages"
    chat_id: Int53
    message_ids: Vector[Int53]
