# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatMessageByDate(BaseObject):
    """
    Returns the last message sent in a chat no later than the specified date
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        date (:class:`int`)
            Point in time (Unix timestamp) relative to which to search for messages
        
    """

    ID: str = Field("getChatMessageByDate", alias="@type")
    chat_id: int
    date: int

    @staticmethod
    def read(q: dict) -> GetChatMessageByDate:
        return GetChatMessageByDate.construct(**q)
