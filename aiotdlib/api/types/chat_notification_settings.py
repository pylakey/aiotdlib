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
    
    Params:
        use_default_mute_for (:class:`bool`)
            If true, mute_for is ignored and the value for the relevant type of chat is used instead
        
        mute_for (:class:`int`)
            Time left before notifications will be unmuted, in seconds
        
        use_default_sound (:class:`bool`)
            If true, sound is ignored and the value for the relevant type of chat is used instead
        
        sound (:class:`str`)
            The name of an audio file to be used for notification sounds; only applies to iOS applications
        
        use_default_show_preview (:class:`bool`)
            If true, show_preview is ignored and the value for the relevant type of chat is used instead
        
        show_preview (:class:`bool`)
            True, if message content should be displayed in notifications
        
        use_default_disable_pinned_message_notifications (:class:`bool`)
            If true, disable_pinned_message_notifications is ignored and the value for the relevant type of chat is used instead
        
        disable_pinned_message_notifications (:class:`bool`)
            If true, notifications for incoming pinned messages will be created as for an ordinary unread message
        
        use_default_disable_mention_notifications (:class:`bool`)
            If true, disable_mention_notifications is ignored and the value for the relevant type of chat is used instead
        
        disable_mention_notifications (:class:`bool`)
            If true, notifications for messages with mentions will be created as for an ordinary unread message
        
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
