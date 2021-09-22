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


class GetChatNotificationSettingsExceptions(BaseObject):
    """
    Returns list of chats with non-default notification settings
    
    :param scope: If specified, only chats from the specified scope will be returned
    :type scope: :class:`NotificationSettingsScope`
    
    :param compare_sound: If true, also chats with non-default sound will be returned
    :type compare_sound: :class:`bool`
    
    """

    ID: str = Field("getChatNotificationSettingsExceptions", alias="@type")
    scope: NotificationSettingsScope
    compare_sound: bool

    @staticmethod
    def read(q: dict) -> GetChatNotificationSettingsExceptions:
        return GetChatNotificationSettingsExceptions.construct(**q)
