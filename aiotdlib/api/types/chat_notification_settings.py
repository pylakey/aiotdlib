# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatNotificationSettings(BaseObject):
    """
    Contains information about notification settings for a chat
    
    :param use_default_mute_for: If true, mute_for is ignored and the value for the relevant type of chat is used instead
    :type use_default_mute_for: :class:`bool`
    
    :param mute_for: Time left before notifications will be unmuted, in seconds
    :type mute_for: :class:`int`
    
    :param use_default_sound: If true, the value for the relevant type of chat is used instead of sound_id
    :type use_default_sound: :class:`bool`
    
    :param sound_id: Identifier of the notification sound to be played; 0 if sound is disabled
    :type sound_id: :class:`int`
    
    :param use_default_show_preview: If true, show_preview is ignored and the value for the relevant type of chat is used instead
    :type use_default_show_preview: :class:`bool`
    
    :param show_preview: True, if message content must be displayed in notifications
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
    sound_id: int
    use_default_show_preview: bool
    show_preview: bool
    use_default_disable_pinned_message_notifications: bool
    disable_pinned_message_notifications: bool
    use_default_disable_mention_notifications: bool
    disable_mention_notifications: bool

    @staticmethod
    def read(q: dict) -> ChatNotificationSettings:
        return ChatNotificationSettings.construct(**q)
