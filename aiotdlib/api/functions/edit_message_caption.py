# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import FormattedText
from ..types import ReplyMarkup
from ..base_object import BaseObject


class EditMessageCaption(BaseObject):
    """
    Edits the message content caption. Returns the edited message after the edit is completed on the server side
    
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reply_markup: The new message reply markup; for bots only
    :type reply_markup: :class:`ReplyMarkup`
    
    :param caption: New message content caption; 0-GetOption("message_caption_length_max") characters
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
