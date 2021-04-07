# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import FormattedText, ReplyMarkup


class EditMessageCaption(BaseObject):
    """
    Edits the message content caption. Returns the edited message after the edit is completed on the server side
    
    Params:
        chat_id (:class:`int`)
            The chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup; for bots only
        
        caption (:class:`FormattedText`)
            New message content caption; 0-GetOption("message_caption_length_max") characters
        
    """

    ID: str = Field("editMessageCaption", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> EditMessageCaption:
        return EditMessageCaption.construct(**q)
