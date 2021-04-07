# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent, ReplyMarkup


class EditMessageText(BaseObject):
    """
    Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side
    
    Params:
        chat_id (:class:`int`)
            The chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup; for bots only
        
        input_message_content (:class:`InputMessageContent`)
            New text content of the message. Should be of type InputMessageText
        
    """

    ID: str = Field("editMessageText", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> EditMessageText:
        return EditMessageText.construct(**q)
