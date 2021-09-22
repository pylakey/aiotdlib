# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_event_action import ChatEventAction
from ..base_object import BaseObject


class ChatEvent(BaseObject):
    """
    Represents a chat event
    
    :param id: Chat event identifier
    :type id: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the event happened
    :type date: :class:`int`
    
    :param user_id: Identifier of the user who performed the action that triggered the event
    :type user_id: :class:`int`
    
    :param action: Action performed by the user
    :type action: :class:`ChatEventAction`
    
    """

    ID: str = Field("chatEvent", alias="@type")
    id: int
    date: int
    user_id: int
    action: ChatEventAction

    @staticmethod
    def read(q: dict) -> ChatEvent:
        return ChatEvent.construct(**q)
