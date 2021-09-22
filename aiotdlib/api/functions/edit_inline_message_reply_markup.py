# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ReplyMarkup
from ..base_object import BaseObject


class EditInlineMessageReplyMarkup(BaseObject):
    """
    Edits the reply markup of an inline message sent via a bot; for bots only
    
    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`str`
    
    :param reply_markup: The new message reply markup
    :type reply_markup: :class:`ReplyMarkup`
    
    """

    ID: str = Field("editInlineMessageReplyMarkup", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup

    @staticmethod
    def read(q: dict) -> EditInlineMessageReplyMarkup:
        return EditInlineMessageReplyMarkup.construct(**q)
