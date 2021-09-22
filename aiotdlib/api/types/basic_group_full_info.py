# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .bot_commands import BotCommands
from .chat_invite_link import ChatInviteLink
from .chat_member import ChatMember
from .chat_photo import ChatPhoto
from ..base_object import BaseObject


class BasicGroupFullInfo(BaseObject):
    """
    Contains full information about a basic group
    
    :param photo: Chat photo; may be null, defaults to None
    :type photo: :class:`ChatPhoto`, optional
    
    :param param_description: Group description. Updated only after the basic group is opened
    :type param_description: :class:`str`
    
    :param creator_user_id: User identifier of the creator of the group; 0 if unknown
    :type creator_user_id: :class:`int`
    
    :param members: Group members
    :type members: :class:`list[ChatMember]`
    
    :param invite_link: Primary invite link for this group; may be null. For chat administrators with can_invite_users right only. Updated only after the basic group is opened, defaults to None
    :type invite_link: :class:`ChatInviteLink`, optional
    
    :param bot_commands: List of commands of bots in the group
    :type bot_commands: :class:`list[BotCommands]`
    
    """

    ID: str = Field("basicGroupFullInfo", alias="@type")
    photo: typing.Optional[ChatPhoto] = None
    param_description: str
    creator_user_id: int
    members: list[ChatMember]
    invite_link: typing.Optional[ChatInviteLink] = None
    bot_commands: list[BotCommands]

    @staticmethod
    def read(q: dict) -> BasicGroupFullInfo:
        return BasicGroupFullInfo.construct(**q)
