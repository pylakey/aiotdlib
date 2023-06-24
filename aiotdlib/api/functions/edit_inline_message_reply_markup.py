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
    ReplyMarkup,
)


class EditInlineMessageReplyMarkup(BaseObject):
    """
    Edits the reply markup of an inline message sent via a bot; for bots only

    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`String`
    :param reply_markup: The new message reply markup; pass null if none, defaults to None
    :type reply_markup: :class:`ReplyMarkup`, optional
    """

    ID: typing.Literal["editInlineMessageReplyMarkup"] = "editInlineMessageReplyMarkup"
    inline_message_id: String
    reply_markup: typing.Optional[ReplyMarkup] = None
