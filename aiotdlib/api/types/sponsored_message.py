# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_invite_link_info import ChatInviteLinkInfo
from .internal_link_type import InternalLinkType
from .message_content import MessageContent
from ..base_object import BaseObject


class SponsoredMessage(BaseObject):
    """
    Describes a sponsored message
    
    :param message_id: Message identifier; unique for the chat to which the sponsored message belongs among both ordinary and sponsored messages
    :type message_id: :class:`int`
    
    :param is_recommended: True, if the message needs to be labeled as "recommended" instead of "sponsored"
    :type is_recommended: :class:`bool`
    
    :param sponsor_chat_id: Sponsor chat identifier; 0 if the sponsor chat is accessible through an invite link
    :type sponsor_chat_id: :class:`int`
    
    :param sponsor_chat_info: Information about the sponsor chat; may be null unless sponsor_chat_id == 0, defaults to None
    :type sponsor_chat_info: :class:`ChatInviteLinkInfo`, optional
    
    :param link: An internal link to be opened when the sponsored message is clicked; may be null if the sponsor chat needs to be opened instead, defaults to None
    :type link: :class:`InternalLinkType`, optional
    
    :param content: Content of the message. Currently, can be only of the type messageText
    :type content: :class:`MessageContent`
    
    """

    ID: str = Field("sponsoredMessage", alias="@type")
    message_id: int
    is_recommended: bool
    sponsor_chat_id: int
    sponsor_chat_info: typing.Optional[ChatInviteLinkInfo] = None
    link: typing.Optional[InternalLinkType] = None
    content: MessageContent

    @staticmethod
    def read(q: dict) -> SponsoredMessage:
        return SponsoredMessage.construct(**q)
