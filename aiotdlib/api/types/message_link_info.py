# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .message import Message
from ..base_object import BaseObject


class MessageLinkInfo(BaseObject):
    """
    Contains information about a link to a message in a chat
    
    :param is_public: True, if the link is a public link for a message in a chat
    :type is_public: :class:`bool`
    
    :param chat_id: If found, identifier of the chat to which the message belongs, 0 otherwise
    :type chat_id: :class:`int`
    
    :param message: If found, the linked message; may be null, defaults to None
    :type message: :class:`Message`, optional
    
    :param media_timestamp: Timestamp from which the video/audio/video note/voice note playing should start, in seconds; 0 if not specified. The media can be in the message content or in its web page preview
    :type media_timestamp: :class:`int`
    
    :param for_album: True, if the whole media album to which the message belongs is linked
    :type for_album: :class:`bool`
    
    :param for_comment: True, if the message is linked as a channel post comment or from a message thread
    :type for_comment: :class:`bool`
    
    """

    ID: str = Field("messageLinkInfo", alias="@type")
    is_public: bool
    chat_id: int
    message: typing.Optional[Message] = None
    media_timestamp: int
    for_album: bool
    for_comment: bool

    @staticmethod
    def read(q: dict) -> MessageLinkInfo:
        return MessageLinkInfo.construct(**q)
