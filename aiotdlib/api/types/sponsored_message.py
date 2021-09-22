# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message_content import MessageContent
from ..base_object import BaseObject


class SponsoredMessage(BaseObject):
    """
    Describes a sponsored message
    
    :param id: Unique sponsored message identifier
    :type id: :class:`int`
    
    :param sponsor_chat_id: Chat identifier
    :type sponsor_chat_id: :class:`int`
    
    :param start_parameter: Parameter for the bot start message if the sponsored chat is a chat with a bot
    :type start_parameter: :class:`str`
    
    :param content: Content of the message
    :type content: :class:`MessageContent`
    
    """

    ID: str = Field("sponsoredMessage", alias="@type")
    id: int
    sponsor_chat_id: int
    start_parameter: str
    content: MessageContent

    @staticmethod
    def read(q: dict) -> SponsoredMessage:
        return SponsoredMessage.construct(**q)
