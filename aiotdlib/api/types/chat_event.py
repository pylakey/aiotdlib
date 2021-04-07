# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_event_action import ChatEventAction
from ..base_object import BaseObject


class ChatEvent(BaseObject):
    """
    Represents a chat event
    
    Params:
        id (:class:`int`)
            Chat event identifier
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the event happened
        
        user_id (:class:`int`)
            Identifier of the user who performed the action that triggered the event
        
        action (:class:`ChatEventAction`)
            Action performed by the user
        
    """

    ID: str = Field("chatEvent", alias="@type")
    id: int
    date: int
    user_id: int
    action: ChatEventAction

    @staticmethod
    def read(q: dict) -> ChatEvent:
        return ChatEvent.construct(**q)
