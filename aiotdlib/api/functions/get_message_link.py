# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetMessageLink(BaseObject):
    """
    Returns an HTTPS link to a message in a chat. Available only for already sent messages in supergroups and channels, or if message.can_get_media_timestamp_links and a media timestamp link is generated. This is an offline request

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param media_timestamp: If not 0, timestamp from which the video/audio/video note/voice note playing must start, in seconds. The media can be in the message content or in its web page preview
    :type media_timestamp: :class:`Int32`
    :param for_album: Pass true to create a link for the whole media album
    :type for_album: :class:`Bool`
    :param in_message_thread: Pass true to create a link to the message as a channel post comment, in a message thread, or a forum topic
    :type in_message_thread: :class:`Bool`
    """

    ID: typing.Literal["getMessageLink"] = "getMessageLink"
    chat_id: Int53
    message_id: Int53
    media_timestamp: Int32 = 0
    for_album: Bool = False
    in_message_thread: Bool = False
