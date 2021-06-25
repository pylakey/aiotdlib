# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent
from ..types import MessageSendOptions


class SendMessageAlbum(BaseObject):
    """
    Sends 2-10 messages grouped together into an album. Currently only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages
    
    Params:
        chat_id (:class:`int`)
            Target chat
        
        message_thread_id (:class:`int`)
            If not 0, a message thread identifier in which the messages will be sent
        
        reply_to_message_id (:class:`int`)
            Identifier of a message to reply to or 0
        
        options (:class:`MessageSendOptions`)
            Options to be used to send the messages
        
        input_message_contents (:obj:`list[InputMessageContent]`)
            Contents of messages to be sent. At most 10 messages can be added to an album
        
    """

    ID: str = Field("sendMessageAlbum", alias="@type")
    chat_id: int
    message_thread_id: int
    reply_to_message_id: int
    options: MessageSendOptions
    input_message_contents: list[InputMessageContent]

    @staticmethod
    def read(q: dict) -> SendMessageAlbum:
        return SendMessageAlbum.construct(**q)
