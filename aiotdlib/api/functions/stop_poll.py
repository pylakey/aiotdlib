# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ReplyMarkup


class StopPoll(BaseObject):
    """
    Stops a poll. A poll in a message can be stopped when the message has can_be_edited flag set
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat to which the poll belongs
        
        message_id (:class:`int`)
            Identifier of the message containing the poll
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup; for bots only
        
    """

    ID: str = Field("stopPoll", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup

    @staticmethod
    def read(q: dict) -> StopPoll:
        return StopPoll.construct(**q)
