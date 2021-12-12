# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatAvailableMessageSenders(BaseObject):
    """
    Returns list of message sender identifiers, which can be used to send messages in a chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChatAvailableMessageSenders", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatAvailableMessageSenders:
        return GetChatAvailableMessageSenders.construct(**q)
