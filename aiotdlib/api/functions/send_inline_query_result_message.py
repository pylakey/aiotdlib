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
    
    Params:
        chat_id (:class:`int`)
            Target chat
        
        message_thread_id (:class:`int`)
            If not 0, a message thread identifier in which the message will be sent
        
        reply_to_message_id (:class:`int`)
            Identifier of a message to reply to or 0
        
        options (:class:`MessageSendOptions`)
            Options to be used to send the message
        
        query_id (:class:`int`)
            Identifier of the inline query
        
        result_id (:class:`str`)
            Identifier of the inline result
        
        hide_via_bot (:class:`bool`)
            If true, there will be no mention of a bot, via which the message is sent. Can be used only for bots GetOption("animation_search_bot_username"), GetOption("photo_search_bot_username") and GetOption("venue_search_bot_username")
        
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
