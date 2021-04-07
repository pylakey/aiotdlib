# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import FormattedText, ReplyMarkup


class EditInlineMessageCaption(BaseObject):
    """
    Edits the caption of an inline message sent via a bot; for bots only
    
    Params:
        inline_message_id (:class:`str`)
            Inline message identifier
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup
        
        caption (:class:`FormattedText`)
            New message content caption; 0-GetOption("message_caption_length_max") characters
        
    """

    ID: str = Field("editInlineMessageCaption", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> EditInlineMessageCaption:
        return EditInlineMessageCaption.construct(**q)
