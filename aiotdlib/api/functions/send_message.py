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
    MessageReplyTo,
    MessageSendOptions,
    ReplyMarkup,
)


class SendMessage(BaseObject):
    """
    Sends a message. Returns the sent message

    :param chat_id: Target chat
    :type chat_id: :class:`Int53`
    :param input_message_content: The content of the message to be sent
    :type input_message_content: :class:`InputMessageContent`
    :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
    :type message_thread_id: :class:`Int53`
    :param reply_to: Identifier of the replied message or story; pass null if none, defaults to None
    :type reply_to: :class:`MessageReplyTo`, optional
    :param options: Options to be used to send the message; pass null to use default options, defaults to None
    :type options: :class:`MessageSendOptions`, optional
    :param reply_markup: Markup for replying to the message; pass null if none; for bots only, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["sendMessage"] = "sendMessage"
    chat_id: Int53
    input_message_content: InputMessageContent
    message_thread_id: Int53 = 0
    reply_to: typing.Optional[MessageReplyTo] = None
    options: typing.Optional[MessageSendOptions] = None
    reply_markup: typing.Optional[ReplyMarkup] = None
