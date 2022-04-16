# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ScopeNotificationSettings(BaseObject):
    """
    Contains information about notification settings for several chats
    
    :param mute_for: Time left before notifications will be unmuted, in seconds
    :type mute_for: :class:`int`
    
    :param sound_id: Identifier of the notification sound to be played; 0 if sound is disabled
    :type sound_id: :class:`int`
    
    :param show_preview: True, if message content must be displayed in notifications
    :type show_preview: :class:`bool`
    
    :param disable_pinned_message_notifications: True, if notifications for incoming pinned messages will be created as for an ordinary unread message
    :type disable_pinned_message_notifications: :class:`bool`
    
    :param disable_mention_notifications: True, if notifications for messages with mentions will be created as for an ordinary unread message
    :type disable_mention_notifications: :class:`bool`
    
    """

    ID: str = Field("scopeNotificationSettings", alias="@type")
    mute_for: int
    sound_id: int
    show_preview: bool
    disable_pinned_message_notifications: bool
    disable_mention_notifications: bool

    @staticmethod
    def read(q: dict) -> ScopeNotificationSettings:
        return ScopeNotificationSettings.construct(**q)
