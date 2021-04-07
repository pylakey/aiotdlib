# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatNotificationSettings


class SetChatNotificationSettings(BaseObject):
    """
    Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        notification_settings (:class:`ChatNotificationSettings`)
            New notification settings for the chat. If the chat is muted for more than 1 week, it is considered to be muted forever
        
    """

    ID: str = Field("setChatNotificationSettings", alias="@type")
    chat_id: int
    notification_settings: ChatNotificationSettings

    @staticmethod
    def read(q: dict) -> SetChatNotificationSettings:
        return SetChatNotificationSettings.construct(**q)
