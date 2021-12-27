# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_event_action import ChatEventAction
from .message_sender import MessageSender
from ..base_object import BaseObject


class ChatEvent(BaseObject):
    """
    Represents a chat event
    
    :param id: Chat event identifier
    :type id: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the event happened
    :type date: :class:`int`
    
    :param member_id: Identifier of the user or chat who performed the action
    :type member_id: :class:`MessageSender`
    
    :param action: The action
    :type action: :class:`ChatEventAction`
    
    """

    ID: str = Field("chatEvent", alias="@type")
    id: int
    date: int
    member_id: MessageSender
    action: ChatEventAction

    @staticmethod
    def read(q: dict) -> ChatEvent:
        return ChatEvent.construct(**q)
