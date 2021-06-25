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
from .chat_location import ChatLocation
from .chat_photo import ChatPhoto
from ..base_object import BaseObject


class SupergroupFullInfo(BaseObject):
    """
    Contains full information about a supergroup or channel
    
    Params:
        photo (:class:`ChatPhoto`)
            Chat photo; may be null
        
        param_description (:class:`str`)
            Supergroup or channel description
        
        member_count (:class:`int`)
            Number of members in the supergroup or channel; 0 if unknown
        
        administrator_count (:class:`int`)
            Number of privileged users in the supergroup or channel; 0 if unknown
        
        restricted_count (:class:`int`)
            Number of restricted users in the supergroup; 0 if unknown
        
        banned_count (:class:`int`)
            Number of users banned from chat; 0 if unknown
        
        linked_chat_id (:class:`int`)
            Chat identifier of a discussion group for the channel, or a channel, for which the supergroup is the designated discussion group; 0 if none or unknown
        
        slow_mode_delay (:class:`int`)
            Delay between consecutive sent messages for non-administrator supergroup members, in seconds
        
        slow_mode_delay_expires_in (:class:`float`)
            Time left before next message can be sent in the supergroup, in seconds. An updateSupergroupFullInfo update is not triggered when value of this field changes, but both new and old values are non-zero
        
        can_get_members (:class:`bool`)
            True, if members of the chat can be retrieved
        
        can_set_username (:class:`bool`)
            True, if the chat username can be changed
        
        can_set_sticker_set (:class:`bool`)
            True, if the supergroup sticker set can be changed
        
        can_set_location (:class:`bool`)
            True, if the supergroup location can be changed
        
        can_get_statistics (:class:`bool`)
            True, if the supergroup or channel statistics are available
        
        is_all_history_available (:class:`bool`)
            True, if new chat members will have access to old messages. In public or discussion groups and both public and private channels, old messages are always available, so this option affects only private supergroups without a linked chat. The value of this field is only available for chat administrators
        
        sticker_set_id (:class:`int`)
            Identifier of the supergroup sticker set; 0 if none
        
        location (:class:`ChatLocation`)
            Location to which the supergroup is connected; may be null
        
        invite_link (:class:`ChatInviteLink`)
            Primary invite link for this chat; may be null. For chat administrators with can_invite_users right only
        
        bot_commands (:obj:`list[BotCommands]`)
            List of commands of bots in the group
        
        upgraded_from_basic_group_id (:class:`int`)
            Identifier of the basic group from which supergroup was upgraded; 0 if none
        
        upgraded_from_max_message_id (:class:`int`)
            Identifier of the last message in the basic group from which supergroup was upgraded; 0 if none
        
    """

    ID: str = Field("supergroupFullInfo", alias="@type")
    photo: typing.Optional[ChatPhoto] = None
    param_description: str
    member_count: int
    administrator_count: int
    restricted_count: int
    banned_count: int
    linked_chat_id: int
    slow_mode_delay: int
    slow_mode_delay_expires_in: float
    can_get_members: bool
    can_set_username: bool
    can_set_sticker_set: bool
    can_set_location: bool
    can_get_statistics: bool
    is_all_history_available: bool
    sticker_set_id: int
    location: typing.Optional[ChatLocation] = None
    invite_link: typing.Optional[ChatInviteLink] = None
    bot_commands: list[BotCommands]
    upgraded_from_basic_group_id: int
    upgraded_from_max_message_id: int

    @staticmethod
    def read(q: dict) -> SupergroupFullInfo:
        return SupergroupFullInfo.construct(**q)
