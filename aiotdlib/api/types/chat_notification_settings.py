# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatNotificationSettings(BaseObject):
    """
    Contains information about notification settings for a chat
    
    :param use_default_mute_for: If true, mute_for is ignored and the value for the relevant type of chat is used instead
    :type use_default_mute_for: :class:`bool`
    
    :param mute_for: Time left before notifications will be unmuted, in seconds
    :type mute_for: :class:`int`
    
    :param use_default_sound: If true, sound is ignored and the value for the relevant type of chat is used instead
    :type use_default_sound: :class:`bool`
    
    :param sound: The name of an audio file to be used for notification sounds; only applies to iOS applications
    :type sound: :class:`str`
    
    :param use_default_show_preview: If true, show_preview is ignored and the value for the relevant type of chat is used instead
    :type use_default_show_preview: :class:`bool`
    
    :param show_preview: True, if message content should be displayed in notifications
    :type show_preview: :class:`bool`
    
    :param use_default_disable_pinned_message_notifications: If true, disable_pinned_message_notifications is ignored and the value for the relevant type of chat is used instead
    :type use_default_disable_pinned_message_notifications: :class:`bool`
    
    :param disable_pinned_message_notifications: If true, notifications for incoming pinned messages will be created as for an ordinary unread message
    :type disable_pinned_message_notifications: :class:`bool`
    
    :param use_default_disable_mention_notifications: If true, disable_mention_notifications is ignored and the value for the relevant type of chat is used instead
    :type use_default_disable_mention_notifications: :class:`bool`
    
    :param disable_mention_notifications: If true, notifications for messages with mentions will be created as for an ordinary unread message
    :type disable_mention_notifications: :class:`bool`
    
    """

    ID: str = Field("chatNotificationSettings", alias="@type")
    use_default_mute_for: bool
    mute_for: int
    use_default_sound: bool
    sound: str
    use_default_show_preview: bool
    show_preview: bool
    use_default_disable_pinned_message_notifications: bool
    disable_pinned_message_notifications: bool
    use_default_disable_mention_notifications: bool
    disable_mention_notifications: bool

    @staticmethod
    def read(q: dict) -> ChatNotificationSettings:
        return ChatNotificationSettings.construct(**q)
