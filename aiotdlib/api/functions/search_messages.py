# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatList
from ..types import SearchMessagesFilter
from ..base_object import BaseObject


class SearchMessages(BaseObject):
    """
    Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    
    :param chat_list: Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported
    :type chat_list: :class:`ChatList`
    
    :param query: Query to search for
    :type query: :class:`str`
    
    :param offset_date: The date of the message starting from which the results should be fetched. Use 0 or any date in the future to get results from the last message
    :type offset_date: :class:`int`
    
    :param offset_chat_id: The chat identifier of the last found message, or 0 for the first request
    :type offset_chat_id: :class:`int`
    
    :param offset_message_id: The message identifier of the last found message, or 0 for the first request
    :type offset_message_id: :class:`int`
    
    :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`int`
    
    :param filter_: Filter for message content in the search results; searchMessagesFilterCall, searchMessagesFilterMissedCall, searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterFailedToSend and searchMessagesFilterPinned are unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    
    :param min_date: If not 0, the minimum date of the messages to return
    :type min_date: :class:`int`
    
    :param max_date: If not 0, the maximum date of the messages to return
    :type max_date: :class:`int`
    
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
