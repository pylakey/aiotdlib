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


class EditMessageReplyMarkup(BaseObject):
    """
    Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side
    
    :param chat_id: The chat the message belongs to
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param reply_markup: The new message reply markup
    :type reply_markup: :class:`ReplyMarkup`
    
    """

    ID: str = Field("editMessageReplyMarkup", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup

    @staticmethod
    def read(q: dict) -> EditMessageReplyMarkup:
        return EditMessageReplyMarkup.construct(**q)
