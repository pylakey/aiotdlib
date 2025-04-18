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
    FormattedText,
    ReplyMarkup,
)


class EditBusinessMessageCaption(BaseObject):
    """
    Edits the caption of a message sent on behalf of a business account; for bots only

    :param business_connection_id: Unique identifier of business connection on behalf of which the message was sent
    :type business_connection_id: :class:`String`
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param show_caption_above_media: Pass true to show the caption above the media; otherwise, the caption will be shown below the media. May be true only for animation, photo, and video messages
    :type show_caption_above_media: :class:`Bool`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    :param caption: New message content caption; pass null to remove caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["editBusinessMessageCaption"] = Field(
        "editBusinessMessageCaption", validation_alias="@type", alias="@type"
    )
    business_connection_id: String
    chat_id: Int53
    message_id: Int53
    show_caption_above_media: Bool = False
    reply_markup: typing.Optional[ReplyMarkup] = None
    caption: typing.Optional[FormattedText] = None
