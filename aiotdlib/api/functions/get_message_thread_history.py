# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessageThreadHistory(BaseObject):
    """
    Returns messages in a message thread of a message. Can be used only if message.can_get_message_thread == true. Message thread of a channel message is in the channel's linked supergroup. The messages are returned in a reverse chronological order (i.e., in order of decreasing message_id). For optimal performance the number of returned messages is chosen by the library
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        message_id (:class:`int`)
            Message identifier, which thread history needs to be returned
        
        from_message_id (:class:`int`)
            Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        
        offset (:class:`int`)
            Specify 0 to get results from exactly the from_message_id or a negative offset up to 99 to get additionally some newer messages
        
        limit (:class:`int`)
            The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. Fewer messages may be returned than specified by the limit, even if the end of the message thread history has not been reached
        
    """

    ID: str = Field("getMessageThreadHistory", alias="@type")
    chat_id: int
    message_id: int
    from_message_id: int
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetMessageThreadHistory:
        return GetMessageThreadHistory.construct(**q)
