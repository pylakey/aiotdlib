# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent
from ..types import ReplyMarkup


class EditMessageText(BaseObject):
    """
    Edits the text of a message (or a text of a game message). Returns the edited message after the edit is completed on the server side
    
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reply_markup: The new message reply markup; pass null if none; for bots only
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: New text content of the message. Must be of type inputMessageText
    :type input_message_content: :class:`InputMessageContent`
    
    """

    ID: str = Field("editMessageText", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> EditMessageText:
        return EditMessageText.construct(**q)
