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


class EditMessageCaption(BaseObject):
    """
    Edits the message content caption. Returns the edited message after the edit is completed on the server side
    
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reply_markup: The new message reply markup; pass null if none; for bots only
    :type reply_markup: :class:`ReplyMarkup`
    
    :param caption: New message content caption; 0-GetOption("message_caption_length_max") characters; pass null to remove caption
    :type caption: :class:`FormattedText`
    
    """

    ID: str = Field("editMessageCaption", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup
    caption: FormattedText

    @staticmethod
    def read(q: dict) -> EditMessageCaption:
        return EditMessageCaption.construct(**q)
