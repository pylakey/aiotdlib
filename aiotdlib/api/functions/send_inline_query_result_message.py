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
    MessageReplyTo,
    MessageSendOptions,
)


class SendInlineQueryResultMessage(BaseObject):
    """
    Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message

    :param chat_id: Target chat
    :type chat_id: :class:`Int53`
    :param query_id: Identifier of the inline query
    :type query_id: :class:`Int64`
    :param result_id: Identifier of the inline query result
    :type result_id: :class:`String`
    :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
    :type message_thread_id: :class:`Int53`
    :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots getOption("animation_search_bot_username"), getOption("photo_search_bot_username"), and getOption("venue_search_bot_username")
    :type hide_via_bot: :class:`Bool`
    :param reply_to: Identifier of the replied message or story; pass null if none, defaults to None
    :type reply_to: :class:`MessageReplyTo`, optional
    :param options: Options to be used to send the message; pass null to use default options, defaults to None
    :type options: :class:`MessageSendOptions`, optional
    """

    ID: typing.Literal["sendInlineQueryResultMessage"] = "sendInlineQueryResultMessage"
    chat_id: Int53
    query_id: Int64
    result_id: String
    message_thread_id: Int53 = 0
    hide_via_bot: Bool = False
    reply_to: typing.Optional[MessageReplyTo] = None
    options: typing.Optional[MessageSendOptions] = None
