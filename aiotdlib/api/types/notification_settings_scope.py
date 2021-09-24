# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class NotificationSettingsScope(BaseObject):
    """
    Describes the types of chats to which notification settings are relevant
    
    """

    ID: str = Field("notificationSettingsScope", alias="@type")


class NotificationSettingsScopeChannelChats(NotificationSettingsScope):
    """
    Notification settings applied to all channels when the corresponding chat setting has a default value
    
    """

    ID: str = Field("notificationSettingsScopeChannelChats", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationSettingsScopeChannelChats:
        return NotificationSettingsScopeChannelChats.construct(**q)


class NotificationSettingsScopeGroupChats(NotificationSettingsScope):
    """
    Notification settings applied to all basic groups and supergroups when the corresponding chat setting has a default value
    
    """

    ID: str = Field("notificationSettingsScopeGroupChats", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationSettingsScopeGroupChats:
        return NotificationSettingsScopeGroupChats.construct(**q)


class NotificationSettingsScopePrivateChats(NotificationSettingsScope):
    """
    Notification settings applied to all private and secret chats when the corresponding chat setting has a default value
    
    """

    ID: str = Field("notificationSettingsScopePrivateChats", alias="@type")

    @staticmethod
    def read(q: dict) -> NotificationSettingsScopePrivateChats:
        return NotificationSettingsScopePrivateChats.construct(**q)
