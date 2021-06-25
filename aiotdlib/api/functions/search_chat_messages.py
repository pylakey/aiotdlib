# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender
from ..types import SearchMessagesFilter


class SearchChatMessages(BaseObject):
    """
    Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query (searchSecretMessages should be used instead), or without an enabled message database. For optimal performance the number of returned messages is chosen by the library
    
    Params:
        chat_id (:class:`int`)
            Identifier of the chat in which to search messages
        
        query (:class:`str`)
            Query to search for
        
        sender (:class:`MessageSender`)
            If not null, only messages sent by the specified sender will be returned. Not supported in secret chats
        
        from_message_id (:class:`int`)
            Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
        
        offset (:class:`int`)
            Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages
        
        limit (:class:`int`)
            The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
        
        filter_ (:class:`SearchMessagesFilter`)
            Filter for message content in the search results
        
        message_thread_id (:class:`int`)
            If not 0, only messages in the specified thread will be returned; supergroups only
        
    """

    ID: str = Field("searchChatMessages", alias="@type")
    chat_id: int
    query: str
    sender: MessageSender
    from_message_id: int
    offset: int
    limit: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')
    message_thread_id: int

    @staticmethod
    def read(q: dict) -> SearchChatMessages:
        return SearchChatMessages.construct(**q)
