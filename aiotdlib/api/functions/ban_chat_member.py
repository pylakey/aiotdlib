# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import MessageSender
from ..base_object import BaseObject


class BanChatMember(BaseObject):
    """
    Bans a member in a chat. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param member_id: Member identifier
    :type member_id: :class:`MessageSender`
    
    :param banned_until_date: Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups
    :type banned_until_date: :class:`int`
    
    :param revoke_messages: Pass true to delete all messages in the chat for the user that is being removed. Always true for supergroups and channels
    :type revoke_messages: :class:`bool`
    
    """

    ID: str = Field("banChatMember", alias="@type")
    chat_id: int
    member_id: MessageSender
    banned_until_date: int
    revoke_messages: bool

    @staticmethod
    def read(q: dict) -> BanChatMember:
        return BanChatMember.construct(**q)
