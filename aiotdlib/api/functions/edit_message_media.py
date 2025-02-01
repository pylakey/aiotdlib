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
    ReplyMarkup,
)


class EditMessageMedia(BaseObject):
    """
    Edits the media content of a message, including message caption. If only the caption needs to be edited, use editMessageCaption instead. The type of message content in an album can't be changed with exception of replacing a photo with a video or vice versa. Returns the edited message after the edit is completed on the server side

    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message. Use messageProperties.can_edit_media to check whether the message can be edited
    :type message_id: :class:`Int53`
    :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["editMessageMedia"] = Field("editMessageMedia", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None
