# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputTextQuote,
)


class ResendMessages(BaseObject):
    """
    Resends messages which failed to send. Can be called only for messages for which messageSendingStateFailed.can_retry is true and after specified in messageSendingStateFailed.retry_after time passed. If a message is re-sent, the corresponding failed to send message is deleted. Returns the sent messages in the same order as the message identifiers passed in message_ids. If a message can't be re-sent, null will be returned instead of the message

    :param chat_id: Identifier of the chat to send messages
    :type chat_id: :class:`Int53`
    :param message_ids: Identifiers of the messages to resend. Message identifiers must be in a strictly increasing order
    :type message_ids: :class:`Vector[Int53]`
    :param paid_message_star_count: The number of Telegram Stars the user agreed to pay to send the messages. Ignored if messageSendingStateFailed.required_paid_message_star_count == 0
    :type paid_message_star_count: :class:`Int53`
    :param quote: New manually chosen quote from the message to be replied; pass null if none. Ignored if more than one message is re-sent, or if messageSendingStateFailed.need_another_reply_quote == false, defaults to None
    :type quote: :class:`InputTextQuote`, optional
    """

    ID: typing.Literal["resendMessages"] = Field("resendMessages", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_ids: Vector[Int53]
    paid_message_star_count: Int53
    quote: typing.Optional[InputTextQuote] = None
