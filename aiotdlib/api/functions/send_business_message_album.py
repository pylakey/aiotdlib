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
)


class SendBusinessMessageAlbum(BaseObject):
    """
    Sends 2-10 messages grouped together into an album on behalf of a business account; for bots only. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages

    :param business_connection_id: Unique identifier of business connection on behalf of which to send the request
    :type business_connection_id: :class:`String`
    :param chat_id: Target chat
    :type chat_id: :class:`Int53`
    :param effect_id: Identifier of the effect to apply to the message
    :type effect_id: :class:`Int64`
    :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album. All messages must have the same value of show_caption_above_media
    :type input_message_contents: :class:`Vector[InputMessageContent]`
    :param disable_notification: Pass true to disable notification for the message
    :type disable_notification: :class:`Bool`
    :param protect_content: Pass true if the content of the message must be protected from forwarding and saving
    :type protect_content: :class:`Bool`
    :param reply_to: Information about the message to be replied; pass null if none, defaults to None
    :type reply_to: :class:`InputMessageReplyTo`, optional
    """

    ID: typing.Literal["sendBusinessMessageAlbum"] = Field(
        "sendBusinessMessageAlbum", validation_alias="@type", alias="@type"
    )
    business_connection_id: String
    chat_id: Int53
    effect_id: Int64
    input_message_contents: Vector[InputMessageContent]
    disable_notification: Bool = False
    protect_content: Bool = False
    reply_to: typing.Optional[InputMessageReplyTo] = None
