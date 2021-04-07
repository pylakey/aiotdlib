# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatStatisticsMessageSenderInfo(BaseObject):
    """
    Contains statistics about messages sent by a user
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        sent_message_count (:class:`int`)
            Number of sent messages
        
        average_character_count (:class:`int`)
            Average number of characters in sent messages
        
    """

    ID: str = Field("chatStatisticsMessageSenderInfo", alias="@type")
    user_id: int
    sent_message_count: int
    average_character_count: int

    @staticmethod
    def read(q: dict) -> ChatStatisticsMessageSenderInfo:
        return ChatStatisticsMessageSenderInfo.construct(**q)
