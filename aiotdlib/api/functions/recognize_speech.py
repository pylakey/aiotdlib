# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RecognizeSpeech(BaseObject):
    """
    Recognizes speech in a voice note message. The message must be successfully sent and must not be scheduled. May return an error with a message "MSG_VOICE_TOO_LONG" if the voice note is too long to be recognized
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    """

    ID: str = Field("recognizeSpeech", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> RecognizeSpeech:
        return RecognizeSpeech.construct(**q)
