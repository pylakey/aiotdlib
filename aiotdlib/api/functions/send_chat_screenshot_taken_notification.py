# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SendChatScreenshotTakenNotification(BaseObject):
    """
    Sends a notification about a screenshot taken in a chat. Supported only in private and secret chats
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("sendChatScreenshotTakenNotification", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> SendChatScreenshotTakenNotification:
        return SendChatScreenshotTakenNotification.construct(**q)
