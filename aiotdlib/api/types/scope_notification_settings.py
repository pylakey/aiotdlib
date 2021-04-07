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
    
    Params:
        mute_for (:class:`int`)
            Time left before notifications will be unmuted, in seconds
        
        sound (:class:`str`)
            The name of an audio file to be used for notification sounds; only applies to iOS applications
        
        show_preview (:class:`bool`)
            True, if message content should be displayed in notifications
        
        disable_pinned_message_notifications (:class:`bool`)
            True, if notifications for incoming pinned messages will be created as for an ordinary unread message
        
        disable_mention_notifications (:class:`bool`)
            True, if notifications for messages with mentions will be created as for an ordinary unread message
        
    """

    ID: str = Field("scopeNotificationSettings", alias="@type")
    mute_for: int
    sound: str
    show_preview: bool
    disable_pinned_message_notifications: bool
    disable_mention_notifications: bool

    @staticmethod
    def read(q: dict) -> ScopeNotificationSettings:
        return ScopeNotificationSettings.construct(**q)
