# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .input_message_content import InputMessageContent
from ..base_object import BaseObject


class DraftMessage(BaseObject):
    """
    Contains information about a message draft
    
    Params:
        reply_to_message_id (:class:`int`)
            Identifier of the message to reply to; 0 if none
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the draft was created
        
        input_message_text (:class:`InputMessageContent`)
            Content of the message draft; this should always be of type inputMessageText
        
    """

    ID: str = Field("draftMessage", alias="@type")
    reply_to_message_id: int
    date: int
    input_message_text: InputMessageContent

    @staticmethod
    def read(q: dict) -> DraftMessage:
        return DraftMessage.construct(**q)
