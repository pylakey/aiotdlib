# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent, MessageSendOptions, ReplyMarkup


class SendMessage(BaseObject):
    """
    Sends a message. Returns the sent message
    
    Params:
        chat_id (:class:`int`)
            Target chat
        
        message_thread_id (:class:`int`)
            If not 0, a message thread identifier in which the message will be sent
        
        reply_to_message_id (:class:`int`)
            Identifier of the message to reply to or 0
        
        options (:class:`MessageSendOptions`)
            Options to be used to send the message
        
        reply_markup (:class:`ReplyMarkup`)
            Markup for replying to the message; for bots only
        
        input_message_content (:class:`InputMessageContent`)
            The content of the message to be sent
        
    """

    ID: str = Field("sendMessage", alias="@type")
    chat_id: int
    message_thread_id: int
    reply_to_message_id: int
    options: MessageSendOptions
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> SendMessage:
        return SendMessage.construct(**q)
