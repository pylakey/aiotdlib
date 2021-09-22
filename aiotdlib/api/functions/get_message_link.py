# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetMessageLink(BaseObject):
    """
    Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels, or if message.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request
    
    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message
    :type message_id: :class:`int`
    
    :param media_timestamp: If not 0, timestamp from which the video/audio/video note/voice note playing should start, in seconds. The media can be in the message content or in its web page preview
    :type media_timestamp: :class:`int`
    
    :param for_album: Pass true to create a link for the whole media album
    :type for_album: :class:`bool`
    
    :param for_comment: Pass true to create a link to the message as a channel post comment, or from a message thread
    :type for_comment: :class:`bool`
    
    """

    ID: str = Field("getMessageLink", alias="@type")
    chat_id: int
    message_id: int
    media_timestamp: int
    for_album: bool
    for_comment: bool

    @staticmethod
    def read(q: dict) -> GetMessageLink:
        return GetMessageLink.construct(**q)
