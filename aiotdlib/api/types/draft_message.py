# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .input_message_content import InputMessageContent
from ..base_object import BaseObject


class DraftMessage(BaseObject):
    """
    Contains information about a message draft
    
    :param reply_to_message_id: Identifier of the message to reply to; 0 if none
    :type reply_to_message_id: :class:`int`
    
    :param date: Point in time (Unix timestamp) when the draft was created
    :type date: :class:`int`
    
    :param input_message_text: Content of the message draft; this should always be of type inputMessageText
    :type input_message_text: :class:`InputMessageContent`
    
    """

    ID: str = Field("draftMessage", alias="@type")
    reply_to_message_id: int
    date: int
    input_message_text: InputMessageContent

    @staticmethod
    def read(q: dict) -> DraftMessage:
        return DraftMessage.construct(**q)
