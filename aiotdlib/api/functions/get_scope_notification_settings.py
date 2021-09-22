# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import NotificationSettingsScope
from ..base_object import BaseObject


class GetScopeNotificationSettings(BaseObject):
    """
    Returns the notification settings for chats of a given type
    
    :param scope: Types of chats for which to return the notification settings information
    :type scope: :class:`NotificationSettingsScope`
    
    """

    ID: str = Field("getScopeNotificationSettings", alias="@type")
    scope: NotificationSettingsScope

    @staticmethod
    def read(q: dict) -> GetScopeNotificationSettings:
        return GetScopeNotificationSettings.construct(**q)
