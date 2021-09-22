# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatStatisticsMessageInteractionInfo(BaseObject):
    """
    Contains statistics about interactions with a message
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param view_count: Number of times the message was viewed
    :type view_count: :class:`int`
    
    :param forward_count: Number of times the message was forwarded
    :type forward_count: :class:`int`
    
    """

    ID: str = Field("chatStatisticsMessageInteractionInfo", alias="@type")
    message_id: int
    view_count: int
    forward_count: int

    @staticmethod
    def read(q: dict) -> ChatStatisticsMessageInteractionInfo:
        return ChatStatisticsMessageInteractionInfo.construct(**q)
