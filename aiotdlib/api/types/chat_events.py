# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_event import ChatEvent
from ..base_object import BaseObject


class ChatEvents(BaseObject):
    """
    Contains a list of chat events
    
    :param events: List of events
    :type events: :class:`list[ChatEvent]`
    
    """

    ID: str = Field("chatEvents", alias="@type")
    events: list[ChatEvent]

    @staticmethod
    def read(q: dict) -> ChatEvents:
        return ChatEvents.construct(**q)
