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
    MessageSendOptions,
)


class SendMessageAlbum(BaseObject):
    """
    Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages

    :param chat_id: Target chat
    :type chat_id: :class:`Int53`
    :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media
    :type input_message_contents: :class:`Vector[InputMessageContent]`
    :param message_thread_id: If not 0, the message thread identifier in which the messages will be sent
    :type message_thread_id: :class:`Int53`
    :param reply_to: Information about the message or story to be replied; pass null if none, defaults to None
    :type reply_to: :class:`InputMessageReplyTo`, optional
    :param options: Options to be used to send the messages; pass null to use default options, defaults to None
    :type options: :class:`MessageSendOptions`, optional
    """

    ID: typing.Literal["sendMessageAlbum"] = Field("sendMessageAlbum", validation_alias="@type", alias="@type")
    chat_id: Int53
    input_message_contents: Vector[InputMessageContent]
    message_thread_id: Int53 = 0
    reply_to: typing.Optional[InputMessageReplyTo] = None
    options: typing.Optional[MessageSendOptions] = None
