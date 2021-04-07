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
    Returns messages in a chat. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance the number of returned messages is chosen by the library. This is an offline request if only_local is true
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        from_message_id (:class:`int`)
            Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        
        offset (:class:`int`)
            Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        
        limit (:class:`int`)
            The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
        
        only_local (:class:`bool`)
            If true, returns only messages that are available locally without sending network requests
        
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
