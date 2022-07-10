# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .attachment_menu_bot_color import AttachmentMenuBotColor
from .file import File
from ..base_object import BaseObject


class AttachmentMenuBot(BaseObject):
    """
    Represents a bot added to attachment menu
    
    :param bot_user_id: User identifier of the bot added to attachment menu
    :type bot_user_id: :class:`int`
    
    :param supports_self_chat: True, if the bot supports opening from attachment menu in the chat with the bot
    :type supports_self_chat: :class:`bool`
    
    :param supports_user_chats: True, if the bot supports opening from attachment menu in private chats with ordinary users
    :type supports_user_chats: :class:`bool`
    
    :param supports_bot_chats: True, if the bot supports opening from attachment menu in private chats with other bots
    :type supports_bot_chats: :class:`bool`
    
    :param supports_group_chats: True, if the bot supports opening from attachment menu in basic group and supergroup chats
    :type supports_group_chats: :class:`bool`
    
    :param supports_channel_chats: True, if the bot supports opening from attachment menu in channel chats
    :type supports_channel_chats: :class:`bool`
    
    :param supports_settings: True, if the bot supports "settings_button_pressed" event
    :type supports_settings: :class:`bool`
    
    :param name: Name for the bot in attachment menu
    :type name: :class:`str`
    
    :param name_color: Color to highlight selected name of the bot if appropriate; may be null, defaults to None
    :type name_color: :class:`AttachmentMenuBotColor`, optional
    
    :param default_icon: Default attachment menu icon for the bot in SVG format; may be null, defaults to None
    :type default_icon: :class:`File`, optional
    
    :param ios_static_icon: Attachment menu icon for the bot in SVG format for the official iOS app; may be null, defaults to None
    :type ios_static_icon: :class:`File`, optional
    
    :param ios_animated_icon: Attachment menu icon for the bot in TGS format for the official iOS app; may be null, defaults to None
    :type ios_animated_icon: :class:`File`, optional
    
    :param android_icon: Attachment menu icon for the bot in TGS format for the official Android app; may be null, defaults to None
    :type android_icon: :class:`File`, optional
    
    :param macos_icon: Attachment menu icon for the bot in TGS format for the official native macOS app; may be null, defaults to None
    :type macos_icon: :class:`File`, optional
    
    :param icon_color: Color to highlight selected icon of the bot if appropriate; may be null, defaults to None
    :type icon_color: :class:`AttachmentMenuBotColor`, optional
    
    :param web_app_placeholder: Default placeholder for opened Web Apps in SVG format; may be null, defaults to None
    :type web_app_placeholder: :class:`File`, optional
    
    """

    ID: str = Field("attachmentMenuBot", alias="@type")
    bot_user_id: int
    supports_self_chat: bool
    supports_user_chats: bool
    supports_bot_chats: bool
    supports_group_chats: bool
    supports_channel_chats: bool
    supports_settings: bool
    name: str
    name_color: typing.Optional[AttachmentMenuBotColor] = None
    default_icon: typing.Optional[File] = None
    ios_static_icon: typing.Optional[File] = None
    ios_animated_icon: typing.Optional[File] = None
    android_icon: typing.Optional[File] = None
    macos_icon: typing.Optional[File] = None
    icon_color: typing.Optional[AttachmentMenuBotColor] = None
    web_app_placeholder: typing.Optional[File] = None

    @staticmethod
    def read(q: dict) -> AttachmentMenuBot:
        return AttachmentMenuBot.construct(**q)
