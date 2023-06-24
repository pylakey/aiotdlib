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


class EditInlineMessageCaption(BaseObject):
    """
    Edits the caption of an inline message sent via a bot; for bots only

    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`String`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    :param caption: New message content caption; pass null to remove caption; 0-getOption("message_caption_length_max") characters, defaults to None
    :type caption: :class:`FormattedText`, optional
    """

    ID: typing.Literal["editInlineMessageCaption"] = "editInlineMessageCaption"
    inline_message_id: String
    reply_markup: typing.Optional[ReplyMarkup] = None
    caption: typing.Optional[FormattedText] = None
