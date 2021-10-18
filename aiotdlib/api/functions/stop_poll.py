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
    
    :param chat_id: Identifier of the chat to which the poll belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message containing the poll
    :type message_id: :class:`int`
    
    :param reply_markup: The new message reply markup; pass null if none; for bots only
    :type reply_markup: :class:`ReplyMarkup`
    
    """

    ID: str = Field("stopPoll", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup

    @staticmethod
    def read(q: dict) -> StopPoll:
        return StopPoll.construct(**q)
