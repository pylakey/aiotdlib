# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetChatMessageTtl(BaseObject):
    """
    Changes the message TTL in a chat. Requires can_delete_messages administrator right in basic groups, supergroups and channels Message TTL can't be changed in a chat with the current user (Saved Messages) and the chat 777000 (Telegram).
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param ttl: New TTL value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400
    :type ttl: :class:`int`
    
    """

    ID: str = Field("setChatMessageTtl", alias="@type")
    chat_id: int
    ttl: int

    @staticmethod
    def read(q: dict) -> SetChatMessageTtl:
        return SetChatMessageTtl.construct(**q)
