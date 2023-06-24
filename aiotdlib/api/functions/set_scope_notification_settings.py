# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    NotificationSettingsScope,
    ScopeNotificationSettings,
)


class SetScopeNotificationSettings(BaseObject):
    """
    Changes notification settings for chats of a given type

    :param scope: Types of chats for which to change the notification settings
    :type scope: :class:`NotificationSettingsScope`
    :param notification_settings: The new notification settings for the given scope
    :type notification_settings: :class:`ScopeNotificationSettings`
    """

    ID: typing.Literal["setScopeNotificationSettings"] = "setScopeNotificationSettings"
    scope: NotificationSettingsScope
    notification_settings: ScopeNotificationSettings
