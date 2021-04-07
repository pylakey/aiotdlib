# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import NotificationSettingsScope, ScopeNotificationSettings


class SetScopeNotificationSettings(BaseObject):
    """
    Changes notification settings for chats of a given type
    
    Params:
        scope (:class:`NotificationSettingsScope`)
            Types of chats for which to change the notification settings
        
        notification_settings (:class:`ScopeNotificationSettings`)
            The new notification settings for the given scope
        
    """

    ID: str = Field("setScopeNotificationSettings", alias="@type")
    scope: NotificationSettingsScope
    notification_settings: ScopeNotificationSettings

    @staticmethod
    def read(q: dict) -> SetScopeNotificationSettings:
        return SetScopeNotificationSettings.construct(**q)
