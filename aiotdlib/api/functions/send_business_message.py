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
    InputMessageContent,
    InputMessageReplyTo,
    ReplyMarkup,
)


class SendBusinessMessage(BaseObject):
    """
    Sends a message on behalf of a business account; for bots only. Returns the message after it was sent

    :param business_connection_id: Unique identifier of business connection on behalf of which to send the request
    :type business_connection_id: :class:`String`
    :param chat_id: Target chat
    :type chat_id: :class:`Int53`
    :param effect_id: Identifier of the effect to apply to the message
    :type effect_id: :class:`Int64`
    :param input_message_content: The content of the message to be sent
    :type input_message_content: :class:`InputMessageContent`
    :param disable_notification: Pass true to disable notification for the message
    :type disable_notification: :class:`Bool`
    :param protect_content: Pass true if the content of the message must be protected from forwarding and saving
    :type protect_content: :class:`Bool`
    :param reply_to: Information about the message to be replied; pass null if none, defaults to None
    :type reply_to: :class:`InputMessageReplyTo`, optional
    :param reply_markup: Markup for replying to the message; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["sendBusinessMessage"] = Field("sendBusinessMessage", validation_alias="@type", alias="@type")
    business_connection_id: String
    chat_id: Int53
    effect_id: Int64
    input_message_content: InputMessageContent
    disable_notification: Bool = False
    protect_content: Bool = False
    reply_to: typing.Optional[InputMessageReplyTo] = None
    reply_markup: typing.Optional[ReplyMarkup] = None
