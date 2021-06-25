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
    
    Params:
        photo (:class:`ChatPhoto`)
            User profile photo; may be null
        
        is_blocked (:class:`bool`)
            True, if the user is blocked by the current user
        
        can_be_called (:class:`bool`)
            True, if the user can be called
        
        supports_video_calls (:class:`bool`)
            True, if a video call can be created with the user
        
        has_private_calls (:class:`bool`)
            True, if the user can't be called due to their privacy settings
        
        need_phone_number_privacy_exception (:class:`bool`)
            True, if the current user needs to explicitly allow to share their phone number with the user when the method addContact is used
        
        bio (:class:`str`)
            A short user bio
        
        share_text (:class:`str`)
            For bots, the text that is shown on the bot's profile page and is sent together with the link when users share the bot
        
        param_description (:class:`str`)
            For bots, the text shown in the chat with the bot if the chat is empty
        
        group_in_common_count (:class:`int`)
            Number of group chats where both the other user and the current user are a member; 0 for the current user
        
        commands (:obj:`list[BotCommand]`)
            For bots, list of the bot commands
        
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
