# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .internal_link_type import InternalLinkType
from .message_content import MessageContent
from ..base_object import BaseObject


class SponsoredMessage(BaseObject):
    """
    Describes a sponsored message
    
    :param id: Unique sponsored message identifier
    :type id: :class:`int`
    
    :param sponsor_chat_id: Chat identifier
    :type sponsor_chat_id: :class:`int`
    
    :param link: An internal link to be opened when the sponsored message is clicked; may be null. If null, the sponsor chat needs to be opened instead, defaults to None
    :type link: :class:`InternalLinkType`, optional
    
    :param content: Content of the message
    :type content: :class:`MessageContent`
    
    """

    ID: str = Field("sponsoredMessage", alias="@type")
    id: int
    sponsor_chat_id: int
    link: typing.Optional[InternalLinkType] = None
    content: MessageContent

    @staticmethod
    def read(q: dict) -> SponsoredMessage:
        return SponsoredMessage.construct(**q)
