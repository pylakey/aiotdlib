# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputMessageContent
from ..types import MessageSendOptions
from ..types import ReplyMarkup
from ..base_object import BaseObject


class SendMessage(BaseObject):
    """
    Sends a message. Returns the sent message
    
    :param chat_id: Target chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
    :type message_thread_id: :class:`int`
    
    :param reply_to_message_id: Identifier of the message to reply to or 0
    :type reply_to_message_id: :class:`int`
    
    :param options: Options to be used to send the message
    :type options: :class:`MessageSendOptions`
    
    :param reply_markup: Markup for replying to the message; for bots only
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: The content of the message to be sent
    :type input_message_content: :class:`InputMessageContent`
    
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
