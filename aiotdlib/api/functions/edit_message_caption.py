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


class EditMessageCaption(BaseObject):
    """
    Edits the message content caption. Returns the edited message after the edit is completed on the server side

    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param reply_markup: The new message reply markup; pass null if none; for bots only, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    :param caption: New message content caption; 0-getOption("message_caption_length_max") characters; pass null to remove caption, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["editMessageCaption"] = "editMessageCaption"
    chat_id: Int53
    message_id: Int53
    reply_markup: typing.Optional[ReplyMarkup] = None
    caption: typing.Optional[FormattedText] = None
