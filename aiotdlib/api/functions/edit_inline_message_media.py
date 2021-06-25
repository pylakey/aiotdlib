# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputMessageContent
from ..types import ReplyMarkup


class EditInlineMessageMedia(BaseObject):
    """
    Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only
    
    Params:
        inline_message_id (:class:`str`)
            Inline message identifier
        
        reply_markup (:class:`ReplyMarkup`)
            The new message reply markup; for bots only
        
        input_message_content (:class:`InputMessageContent`)
            New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
        
    """

    ID: str = Field("editInlineMessageMedia", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> EditInlineMessageMedia:
        return EditInlineMessageMedia.construct(**q)
