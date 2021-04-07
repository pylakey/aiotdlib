# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import NotificationSettingsScope


class GetChatNotificationSettingsExceptions(BaseObject):
    """
    Returns list of chats with non-default notification settings
    
    Params:
        scope (:class:`NotificationSettingsScope`)
            If specified, only chats from the specified scope will be returned
        
        compare_sound (:class:`bool`)
            If true, also chats with non-default sound will be returned
        
    """

    ID: str = Field("getChatNotificationSettingsExceptions", alias="@type")
    scope: NotificationSettingsScope
    compare_sound: bool

    @staticmethod
    def read(q: dict) -> GetChatNotificationSettingsExceptions:
        return GetChatNotificationSettingsExceptions.construct(**q)
