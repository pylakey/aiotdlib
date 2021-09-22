# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatNotificationSettings
from ..base_object import BaseObject


class SetChatNotificationSettings(BaseObject):
    """
    Changes the notification settings of a chat. Notification settings of a chat with the current user (Saved Messages) can't be changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param notification_settings: New notification settings for the chat. If the chat is muted for more than 1 week, it is considered to be muted forever
    :type notification_settings: :class:`ChatNotificationSettings`
    
    """

    ID: str = Field("setChatNotificationSettings", alias="@type")
    chat_id: int
    notification_settings: ChatNotificationSettings

    @staticmethod
    def read(q: dict) -> SetChatNotificationSettings:
        return SetChatNotificationSettings.construct(**q)
