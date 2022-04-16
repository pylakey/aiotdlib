# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSendOptions


class SendInlineQueryResultMessage(BaseObject):
    """
    Sends the result of an inline query as a message. Returns the sent message. Always clears a chat draft message
    
    :param chat_id: Target chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: If not 0, a message thread identifier in which the message will be sent
    :type message_thread_id: :class:`int`
    
    :param reply_to_message_id: Identifier of a replied message; 0 if none
    :type reply_to_message_id: :class:`int`
    
    :param options: Options to be used to send the message; pass null to use default options
    :type options: :class:`MessageSendOptions`
    
    :param query_id: Identifier of the inline query
    :type query_id: :class:`int`
    
    :param result_id: Identifier of the inline result
    :type result_id: :class:`str`
    
    :param hide_via_bot: Pass true to hide the bot, via which the message is sent. Can be used only for bots GetOption("animation_search_bot_username"), GetOption("photo_search_bot_username"), and GetOption("venue_search_bot_username")
    :type hide_via_bot: :class:`bool`
    
    """

    ID: str = Field("sendInlineQueryResultMessage", alias="@type")
    chat_id: int
    message_thread_id: int
    reply_to_message_id: int
    options: MessageSendOptions
    query_id: int
    result_id: str
    hide_via_bot: bool

    @staticmethod
    def read(q: dict) -> SendInlineQueryResultMessage:
        return SendInlineQueryResultMessage.construct(**q)
