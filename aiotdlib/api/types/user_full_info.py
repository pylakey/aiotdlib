# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .bot_command import BotCommand
from .chat_photo import ChatPhoto
from ..base_object import BaseObject


class UserFullInfo(BaseObject):
    """
    Contains full information about a user
    
    :param photo: User profile photo; may be null, defaults to None
    :type photo: :class:`ChatPhoto`, optional
    
    :param is_blocked: True, if the user is blocked by the current user
    :type is_blocked: :class:`bool`
    
    :param can_be_called: True, if the user can be called
    :type can_be_called: :class:`bool`
    
    :param supports_video_calls: True, if a video call can be created with the user
    :type supports_video_calls: :class:`bool`
    
    :param has_private_calls: True, if the user can't be called due to their privacy settings
    :type has_private_calls: :class:`bool`
    
    :param need_phone_number_privacy_exception: True, if the current user needs to explicitly allow to share their phone number with the user when the method addContact is used
    :type need_phone_number_privacy_exception: :class:`bool`
    
    :param bio: A short user bio
    :type bio: :class:`str`
    
    :param share_text: For bots, the text that is shown on the bot's profile page and is sent together with the link when users share the bot
    :type share_text: :class:`str`
    
    :param param_description: For bots, the text shown in the chat with the bot if the chat is empty
    :type param_description: :class:`str`
    
    :param group_in_common_count: Number of group chats where both the other user and the current user are a member; 0 for the current user
    :type group_in_common_count: :class:`int`
    
    :param commands: For bots, list of the bot commands
    :type commands: :class:`list[BotCommand]`
    
    """

    ID: str = Field("userFullInfo", alias="@type")
    photo: typing.Optional[ChatPhoto] = None
    is_blocked: bool
    can_be_called: bool
    supports_video_calls: bool
    has_private_calls: bool
    need_phone_number_privacy_exception: bool
    bio: str
    share_text: str
    param_description: str
    group_in_common_count: int
    commands: list[BotCommand]

    @staticmethod
    def read(q: dict) -> UserFullInfo:
        return UserFullInfo.construct(**q)
