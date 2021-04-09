# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .bot_info import BotInfo
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
            For bots, the text that is included with the link when users share the bot
        
        group_in_common_count (:class:`int`)
            Number of group chats where both the other user and the current user are a member; 0 for the current user
        
        bot_info (:class:`BotInfo`)
            If the user is a bot, information about the bot; may be null
        
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
    group_in_common_count: int
    bot_info: typing.Optional[BotInfo] = None

    @staticmethod
    def read(q: dict) -> UserFullInfo:
        return UserFullInfo.construct(**q)
