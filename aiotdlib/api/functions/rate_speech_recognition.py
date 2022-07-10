# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class RateSpeechRecognition(BaseObject):
    """
    Rates recognized speech in a voice note message
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param is_good: Pass true if the speech recognition is good
    :type is_good: :class:`bool`
    
    """

    ID: str = Field("rateSpeechRecognition", alias="@type")
    chat_id: int
    message_id: int
    is_good: bool

    @staticmethod
    def read(q: dict) -> RateSpeechRecognition:
        return RateSpeechRecognition.construct(**q)
