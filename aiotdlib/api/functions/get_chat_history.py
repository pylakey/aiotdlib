# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatHistory(BaseObject):
    """
    Returns messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance, the number of returned messages is chosen by TDLib. This is an offline request if only_local is true
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
    :type from_message_id: :class:`int`
    
    :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
    :type offset: :class:`int`
    
    :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`int`
    
    :param only_local: Pass true to get only messages that are available without sending network requests
    :type only_local: :class:`bool`
    
    """

    ID: str = Field("getChatHistory", alias="@type")
    chat_id: int
    from_message_id: int
    offset: int
    limit: int
    only_local: bool

    @staticmethod
    def read(q: dict) -> GetChatHistory:
        return GetChatHistory.construct(**q)
