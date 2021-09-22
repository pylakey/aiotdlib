# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatStatisticsMessageSenderInfo(BaseObject):
    """
    Contains statistics about messages sent by a user
    
    :param user_id: User identifier
    :type user_id: :class:`int`
    
    :param sent_message_count: Number of sent messages
    :type sent_message_count: :class:`int`
    
    :param average_character_count: Average number of characters in sent messages; 0 if unknown
    :type average_character_count: :class:`int`
    
    """

    ID: str = Field("chatStatisticsMessageSenderInfo", alias="@type")
    user_id: int
    sent_message_count: int
    average_character_count: int

    @staticmethod
    def read(q: dict) -> ChatStatisticsMessageSenderInfo:
        return ChatStatisticsMessageSenderInfo.construct(**q)
