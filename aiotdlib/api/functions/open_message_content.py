# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class OpenMessageContent(BaseObject):
    """
    Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed
    
    :param chat_id: Chat identifier of the message
    :type chat_id: :class:`int`
    
    :param message_id: Identifier of the message with the opened content
    :type message_id: :class:`int`
    
    """

    ID: str = Field("openMessageContent", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> OpenMessageContent:
        return OpenMessageContent.construct(**q)
