# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class OpenMessageContent(BaseObject):
    """
    Informs TDLib that the message content has been opened (e.g., the user has opened a photo, video, document, location or venue, or has listened to an audio file or voice note message). An updateMessageContentOpened update will be generated if something has changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the message
        
        message_id (:class:`int`)
            Identifier of the message with the opened content
        
    """

    ID: str = Field("openMessageContent", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> OpenMessageContent:
        return OpenMessageContent.construct(**q)
