# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_event import ChatEvent
from ..base_object import BaseObject


class ChatEvents(BaseObject):
    """
    Contains a list of chat events
    
    Params:
        events (:obj:`list[ChatEvent]`)
            List of events
        
    """

    ID: str = Field("chatEvents", alias="@type")
    events: list[ChatEvent]

    @staticmethod
    def read(q: dict) -> ChatEvents:
        return ChatEvents.construct(**q)
