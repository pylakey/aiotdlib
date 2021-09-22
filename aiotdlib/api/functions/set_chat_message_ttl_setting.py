# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetChatMessageTtlSetting(BaseObject):
    """
    Changes the message TTL setting (sets a new self-destruct timer) in a chat. Requires can_delete_messages administrator right in basic groups, supergroups and channels Message TTL setting of a chat with the current user (Saved Messages) and the chat 777000 (Telegram) can't be changed
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param ttl: New TTL value, in seconds; must be one of 0, 86400, 7 * 86400, or 31 * 86400 unless the chat is secret
    :type ttl: :class:`int`
    
    """

    ID: str = Field("setChatMessageTtlSetting", alias="@type")
    chat_id: int
    ttl: int

    @staticmethod
    def read(q: dict) -> SetChatMessageTtlSetting:
        return SetChatMessageTtlSetting.construct(**q)
