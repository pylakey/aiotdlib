# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import NotificationSettingsScope


class GetScopeNotificationSettings(BaseObject):
    """
    Returns the notification settings for chats of a given type
    
    Params:
        scope (:class:`NotificationSettingsScope`)
            Types of chats for which to return the notification settings information
        
    """

    ID: str = Field("getScopeNotificationSettings", alias="@type")
    scope: NotificationSettingsScope

    @staticmethod
    def read(q: dict) -> GetScopeNotificationSettings:
        return GetScopeNotificationSettings.construct(**q)
