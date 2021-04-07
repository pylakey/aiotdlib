# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetMessagePublicForwards(BaseObject):
    """
    Returns forwarded copies of a channel message to different public channels. For optimal performance the number of returned messages is chosen by the library
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the message
        
        message_id (:class:`int`)
            Message identifier
        
        offset (:class:`str`)
            Offset of the first entry to return as received from the previous request; use empty string to get first chunk of results
        
        limit (:class:`int`)
            The maximum number of messages to be returned; must be positive and can't be greater than 100. Fewer messages may be returned than specified by the limit, even if the end of the list has not been reached
        
    """

    ID: str = Field("getMessagePublicForwards", alias="@type")
    chat_id: int
    message_id: int
    offset: str
    limit: int

    @staticmethod
    def read(q: dict) -> GetMessagePublicForwards:
        return GetMessagePublicForwards.construct(**q)
