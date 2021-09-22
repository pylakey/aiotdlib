# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatScheduledMessages(BaseObject):
    """
    Returns all scheduled messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id)
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChatScheduledMessages", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatScheduledMessages:
        return GetChatScheduledMessages.construct(**q)
