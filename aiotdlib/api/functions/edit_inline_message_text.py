# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent, ReplyMarkup


class EditInlineMessageText(BaseObject):
    """
    Edits the text of an inline text or game message sent via a bot; for bots only
    
    Params:
        inline_message_id (:class:`str`)
            Inline message identifier
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup
        
        input_message_content (:class:`InputMessageContent`)
            New text content of the message. Should be of type InputMessageText
        
    """

    ID: str = Field("editInlineMessageText", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> EditInlineMessageText:
        return EditInlineMessageText.construct(**q)
