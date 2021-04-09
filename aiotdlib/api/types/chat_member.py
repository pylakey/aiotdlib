# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .bot_info import BotInfo
from .chat_member_status import ChatMemberStatus
from ..base_object import BaseObject


class ChatMember(BaseObject):
    """
    A user with information about joining/leaving a chat
    
    Params:
        user_id (:class:`int`)
            User identifier of the chat member
        
        inviter_user_id (:class:`int`)
            Identifier of a user that invited/promoted/banned this member in the chat; 0 if unknown
        
        joined_chat_date (:class:`int`)
            Point in time (Unix timestamp) when the user joined the chat
        
        status (:class:`ChatMemberStatus`)
            Status of the member in the chat
        
        bot_info (:class:`BotInfo`)
            If the user is a bot, information about the bot; may be null. Can be null even for a bot if the bot is not the chat member
        
    """

    ID: str = Field("chatMember", alias="@type")
    user_id: int
    inviter_user_id: int
    joined_chat_date: int
    status: ChatMemberStatus
    bot_info: typing.Optional[BotInfo] = None

    @staticmethod
    def read(q: dict) -> ChatMember:
        return ChatMember.construct(**q)
