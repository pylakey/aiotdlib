# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import NotificationSettingsScope
from ..types import ScopeNotificationSettings
from ..base_object import BaseObject


class SetScopeNotificationSettings(BaseObject):
    """
    Changes notification settings for chats of a given type
    
    :param scope: Types of chats for which to change the notification settings
    :type scope: :class:`NotificationSettingsScope`
    
    :param notification_settings: The new notification settings for the given scope
    :type notification_settings: :class:`ScopeNotificationSettings`
    
    """

    ID: str = Field("setScopeNotificationSettings", alias="@type")
    scope: NotificationSettingsScope
    notification_settings: ScopeNotificationSettings

    @staticmethod
    def read(q: dict) -> SetScopeNotificationSettings:
        return SetScopeNotificationSettings.construct(**q)
