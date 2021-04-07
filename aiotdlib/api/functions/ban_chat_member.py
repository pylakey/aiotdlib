# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class BanChatMember(BaseObject):
    """
    Bans a member in a chat. Members can't be banned in private or secret chats. In supergroups and channels, the user will not be able to return to the group on their own using invite links, etc., unless unbanned first
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        user_id (:class:`int`)
            Identifier of the user
        
        banned_until_date (:class:`int`)
            Point in time (Unix timestamp) when the user will be unbanned; 0 if never. If the user is banned for more than 366 days or for less than 30 seconds from the current time, the user is considered to be banned forever. Ignored in basic groups
        
        revoke_messages (:class:`bool`)
            Pass true to delete all messages in the chat for the user. Always true for supergroups and channels
        
    """

    ID: str = Field("banChatMember", alias="@type")
    chat_id: int
    user_id: int
    banned_until_date: int
    revoke_messages: bool

    @staticmethod
    def read(q: dict) -> BanChatMember:
        return BanChatMember.construct(**q)
