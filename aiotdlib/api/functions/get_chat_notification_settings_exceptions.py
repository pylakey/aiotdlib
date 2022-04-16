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
    
    :param scope: If specified, only chats from the scope will be returned; pass null to return chats from all scopes
    :type scope: :class:`NotificationSettingsScope`
    
    :param compare_sound: Pass true to include in the response chats with only non-default sound
    :type compare_sound: :class:`bool`
    
    """

    ID: str = Field("getChatNotificationSettingsExceptions", alias="@type")
    scope: NotificationSettingsScope
    compare_sound: bool

    @staticmethod
    def read(q: dict) -> GetChatNotificationSettingsExceptions:
        return GetChatNotificationSettingsExceptions.construct(**q)
