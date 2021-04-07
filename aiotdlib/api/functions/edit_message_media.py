# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent, ReplyMarkup


class EditMessageMedia(BaseObject):
    """
    Edits the content of a message with an animation, an audio, a document, a photo or a video. The media in the message can't be replaced if the message was set to self-destruct. Media can't be replaced by self-destructing media. Media in an album can be edited only to contain a photo or a video. Returns the edited message after the edit is completed on the server side
    
    Params:
        chat_id (:class:`int`)
            The chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup; for bots only
        
        input_message_content (:class:`InputMessageContent`)
            New content of the message. Must be one of the following types: InputMessageAnimation, InputMessageAudio, InputMessageDocument, InputMessagePhoto or InputMessageVideo
        
    """

    ID: str = Field("editMessageMedia", alias="@type")
    chat_id: int
    message_id: int
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> EditMessageMedia:
        return EditMessageMedia.construct(**q)
