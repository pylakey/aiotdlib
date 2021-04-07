# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatStatisticsMessageInteractionInfo(BaseObject):
    """
    Contains statistics about interactions with a message
    
    Params:
        message_id (:class:`int`)
            Message identifier
        
        view_count (:class:`int`)
            Number of times the message was viewed
        
        forward_count (:class:`int`)
            Number of times the message was forwarded
        
    """

    ID: str = Field("chatStatisticsMessageInteractionInfo", alias="@type")
    message_id: int
    view_count: int
    forward_count: int

    @staticmethod
    def read(q: dict) -> ChatStatisticsMessageInteractionInfo:
        return ChatStatisticsMessageInteractionInfo.construct(**q)
