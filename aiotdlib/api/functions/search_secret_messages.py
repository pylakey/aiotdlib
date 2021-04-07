# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import SearchMessagesFilter


class SearchSecretMessages(BaseObject):
    """
    Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance the number of returned messages is chosen by the library
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat in which to search. Specify 0 to search in all secret chats
        
        query (:class:`str`)
            Query to search for. If empty, searchChatMessages should be used instead
        
        offset (:class:`str`)
            Offset of the first entry to return as received from the previous request; use empty string to get first chunk of results
        
        limit (:class:`int`)
            The maximum number of messages to be returned; up to 100. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
        
        filter_ (:class:`SearchMessagesFilter`)
            A filter for message content in the search results
        
    """

    ID: str = Field("searchSecretMessages", alias="@type")
    chat_id: int
    query: str
    offset: str
    limit: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')

    @staticmethod
    def read(q: dict) -> SearchSecretMessages:
        return SearchSecretMessages.construct(**q)
