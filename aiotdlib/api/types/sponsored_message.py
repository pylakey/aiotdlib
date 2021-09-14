# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .message_content import MessageContent
from ..base_object import BaseObject


class SponsoredMessage(BaseObject):
    """
    Describes a sponsored message
    
    Params:
        id (:class:`int`)
            Unique sponsored message identifier
        
        sponsor_chat_id (:class:`int`)
            Chat identifier
        
        start_parameter (:class:`str`)
            Parameter for the bot start message if the sponsored chat is a chat with a bot
        
        content (:class:`MessageContent`)
            Content of the message
        
    """

    ID: str = Field("sponsoredMessage", alias="@type")
    id: int
    sponsor_chat_id: int
    start_parameter: str
    content: MessageContent

    @staticmethod
    def read(q: dict) -> SponsoredMessage:
        return SponsoredMessage.construct(**q)
