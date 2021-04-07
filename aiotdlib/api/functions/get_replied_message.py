# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetRepliedMessage(BaseObject):
    """
    Returns information about a message that is replied by a given message. Also returns the pinned message, the game message, and the invoice message for messages of the types messagePinMessage, messageGameScore, and messagePaymentSuccessful respectively
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat the message belongs to
        
        message_id (:class:`int`)
            Identifier of the message reply to which to get
        
    """

    ID: str = Field("getRepliedMessage", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetRepliedMessage:
        return GetRepliedMessage.construct(**q)
