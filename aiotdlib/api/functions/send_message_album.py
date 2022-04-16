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
    Sends 2-10 messages grouped together into an album. Currently, only audio, document, photo and video messages can be grouped into an album. Documents and audio files can be only grouped in an album with messages of the same type. Returns sent messages
    
    :param chat_id: Target chat
    :type chat_id: :class:`int`
    
    :param message_thread_id: If not 0, a message thread identifier in which the messages will be sent
    :type message_thread_id: :class:`int`
    
    :param reply_to_message_id: Identifier of a replied message; 0 if none
    :type reply_to_message_id: :class:`int`
    
    :param options: Options to be used to send the messages; pass null to use default options
    :type options: :class:`MessageSendOptions`
    
    :param input_message_contents: Contents of messages to be sent. At most 10 messages can be added to an album
    :type input_message_contents: :class:`list[InputMessageContent]`
    
    :param only_preview: Pass true to get fake messages instead of actually sending them
    :type only_preview: :class:`bool`
    
    """

    ID: str = Field("sendMessageAlbum", alias="@type")
    chat_id: int
    message_thread_id: int
    reply_to_message_id: int
    options: MessageSendOptions
    input_message_contents: list[InputMessageContent]
    only_preview: bool

    @staticmethod
    def read(q: dict) -> SendMessageAlbum:
        return SendMessageAlbum.construct(**q)
