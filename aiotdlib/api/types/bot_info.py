# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .animation import Animation
from .bot_command import BotCommand
from .bot_menu_button import BotMenuButton
from .chat_administrator_rights import ChatAdministratorRights
from .photo import Photo
from ..base_object import BaseObject


class BotInfo(BaseObject):
    """
    Contains information about a bot
    
    :param share_text: The text that is shown on the bot's profile page and is sent together with the link when users share the bot
    :type share_text: :class:`str`
    
    :param param_description: The text shown in the chat with the bot if the chat is empty
    :type param_description: :class:`str`
    
    :param photo: Photo shown in the chat with the bot if the chat is empty; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    
    :param animation: Animation shown in the chat with the bot if the chat is empty; may be null, defaults to None
    :type animation: :class:`Animation`, optional
    
    :param menu_button: Information about a button to show instead of the bot commands menu button; may be null if ordinary bot commands menu must be shown, defaults to None
    :type menu_button: :class:`BotMenuButton`, optional
    
    :param commands: List of the bot commands
    :type commands: :class:`list[BotCommand]`
    
    :param default_group_administrator_rights: Default administrator rights for adding the bot to basic group and supergroup chats; may be null, defaults to None
    :type default_group_administrator_rights: :class:`ChatAdministratorRights`, optional
    
    :param default_channel_administrator_rights: Default administrator rights for adding the bot to channels; may be null, defaults to None
    :type default_channel_administrator_rights: :class:`ChatAdministratorRights`, optional
    
    """

    ID: str = Field("botInfo", alias="@type")
    share_text: str
    param_description: str
    photo: typing.Optional[Photo] = None
    animation: typing.Optional[Animation] = None
    menu_button: typing.Optional[BotMenuButton] = None
    commands: list[BotCommand]
    default_group_administrator_rights: typing.Optional[ChatAdministratorRights] = None
    default_channel_administrator_rights: typing.Optional[ChatAdministratorRights] = None

    @staticmethod
    def read(q: dict) -> BotInfo:
        return BotInfo.construct(**q)
