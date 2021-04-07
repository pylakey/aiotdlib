# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import SearchMessagesFilter


class GetChatMessageCount(BaseObject):
    """
    Returns approximate number of messages of the specified type in the chat
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat in which to count messages
        
        filter_ (:class:`SearchMessagesFilter`)
            Filter for message content; searchMessagesFilterEmpty is unsupported in this function
        
        return_local (:class:`bool`)
            If true, returns count that is available locally without sending network requests, returning -1 if the number of messages is unknown
        
    """

    ID: str = Field("getChatMessageCount", alias="@type")
    chat_id: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')
    return_local: bool

    @staticmethod
    def read(q: dict) -> GetChatMessageCount:
        return GetChatMessageCount.construct(**q)
