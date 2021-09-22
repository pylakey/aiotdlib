# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputMessageContent
from ..types import ReplyMarkup
from ..base_object import BaseObject


class EditInlineMessageMedia(BaseObject):
    """
    Edits the content of a message with an animation, an audio, a document, a photo or a video in an inline message sent via a bot; for bots only
    
    :param inline_message_id: Inline message identifier
    :type inline_message_id: :class:`str`
    
    :param reply_markup: The new message reply markup; for bots only
    :type reply_markup: :class:`ReplyMarkup`
    
    :param input_message_content: New content of the message. Must be one of the following types: inputMessageAnimation, inputMessageAudio, inputMessageDocument, inputMessagePhoto or inputMessageVideo
    :type input_message_content: :class:`InputMessageContent`
    
    """

    ID: str = Field("editInlineMessageMedia", alias="@type")
    inline_message_id: str
    reply_markup: ReplyMarkup
    input_message_content: InputMessageContent

    @staticmethod
    def read(q: dict) -> EditInlineMessageMedia:
        return EditInlineMessageMedia.construct(**q)
