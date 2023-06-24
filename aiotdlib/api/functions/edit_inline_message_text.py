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


class EditInlineMessageText(BaseObject):
    """
    Edits the text of an inline text or game message sent via a bot; for bots only

    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`String`
    :param input_message_content: New text content of the message. Must be of type inputMessageText
    :type input_message_content: :class:`InputMessageContent`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["editInlineMessageText"] = "editInlineMessageText"
    inline_message_id: String
    input_message_content: InputMessageContent
    reply_markup: typing.Optional[ReplyMarkup] = None
