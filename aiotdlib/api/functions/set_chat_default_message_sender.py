# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class SetChatDefaultMessageSender(BaseObject):
    """
    Changes default message sender that is chosen in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param default_message_sender_id: New default message sender in the chat
    :type default_message_sender_id: :class:`MessageSender`
    
    """

    ID: str = Field("setChatDefaultMessageSender", alias="@type")
    chat_id: int
    default_message_sender_id: MessageSender

    @staticmethod
    def read(q: dict) -> SetChatDefaultMessageSender:
        return SetChatDefaultMessageSender.construct(**q)
