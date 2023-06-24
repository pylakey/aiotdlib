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
)


class GetScopeNotificationSettings(BaseObject):
    """
    Returns the notification settings for chats of a given type

    :param scope: Types of chats for which to return the notification settings information
    :type scope: :class:`NotificationSettingsScope`
    """

    ID: typing.Literal["getScopeNotificationSettings"] = "getScopeNotificationSettings"
    scope: NotificationSettingsScope
