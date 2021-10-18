# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import FormattedText
from ..types import ReplyMarkup


class EditInlineMessageCaption(BaseObject):
    """
    Edits the caption of an inline message sent via a bot; for bots only
    
    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`str`
    
    :param reply_markup: The new message reply markup; pass null if none
    :type reply_markup: :class:`ReplyMarkup`
    
    :param caption: New message content caption; pass null to remove caption; 0-GetOption("message_caption_length_max") characters
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("editInlineMessageCaption", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> EditInlineMessageCaption:
        return EditInlineMessageCaption.construct(**q)
