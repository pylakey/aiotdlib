# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class SetChatMessageSender(BaseObject):
    """
    Selects a message sender to send messages in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param message_sender_id: New message sender for the chat
    :type message_sender_id: :class:`MessageSender`
    
    """

    ID: str = Field("setChatMessageSender", alias="@type")
    chat_id: int
    message_sender_id: MessageSender

    @staticmethod
    def read(q: dict) -> SetChatMessageSender:
        return SetChatMessageSender.construct(**q)
