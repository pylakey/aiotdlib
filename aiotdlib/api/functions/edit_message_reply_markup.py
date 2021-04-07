# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ReplyMarkup


class EditMessageReplyMarkup(BaseObject):
    """
    Edits the message reply markup; for bots only. Returns the edited message after the edit is completed on the server side
    
    Params:
        chat_id (:class:`int`)
            The chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup
        
    """

    ID: str = Field("editMessageReplyMarkup", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup

    @staticmethod
    def read(q: dict) -> EditMessageReplyMarkup:
        return EditMessageReplyMarkup.construct(**q)
