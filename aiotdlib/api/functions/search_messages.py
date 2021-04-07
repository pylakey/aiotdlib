# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatList, SearchMessagesFilter


class SearchMessages(BaseObject):
    """
    Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance the number of returned messages is chosen by the library
    
    Params:
        chat_list (:class:`ChatList`)
            Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported
        
        query (:class:`str`)
            Query to search for
        
        offset_date (:class:`int`)
            The date of the message starting from which the results should be fetched. Use 0 or any date in the future to get results from the last message
        
        offset_chat_id (:class:`int`)
            The chat identifier of the last found message, or 0 for the first request
        
        offset_message_id (:class:`int`)
            The message identifier of the last found message, or 0 for the first request
        
        limit (:class:`int`)
            The maximum number of messages to be returned; up to 100. Fewer messages may be returned than specified by the limit, even if the end of the message history has not been reached
        
        filter_ (:class:`SearchMessagesFilter`)
            Filter for message content in the search results; searchMessagesFilterCall, searchMessagesFilterMissedCall, searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterFailedToSend and searchMessagesFilterPinned are unsupported in this function
        
        min_date (:class:`int`)
            If not 0, the minimum date of the messages to return
        
        max_date (:class:`int`)
            If not 0, the maximum date of the messages to return
        
    """

    ID: str = Field("searchMessages", alias="@type")
    chat_list: ChatList
    query: str
    offset_date: int
    offset_chat_id: int
    offset_message_id: int
    limit: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')
    min_date: int
    max_date: int

    @staticmethod
    def read(q: dict) -> SearchMessages:
        return SearchMessages.construct(**q)
