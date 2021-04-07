# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ReplyMarkup


class EditInlineMessageReplyMarkup(BaseObject):
    """
    Edits the reply markup of an inline message sent via a bot; for bots only
    
    Params:
        inline_message_id (:class:`str`)
            Inline message identifier
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup
        
    """

    ID: str = Field("editInlineMessageReplyMarkup", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup

    @staticmethod
    def read(q: dict) -> EditInlineMessageReplyMarkup:
        return EditInlineMessageReplyMarkup.construct(**q)
