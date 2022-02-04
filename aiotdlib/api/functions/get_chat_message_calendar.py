# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import SearchMessagesFilter


class GetChatMessageCalendar(BaseObject):
    """
    Returns information about the next messages of the specified type in the chat split by days. Returns the results in reverse chronological order. Can return partial result for the last returned day. Behavior of this method depends on the value of the option "utc_time_offset"
    
    :param chat_id: Identifier of the chat in which to return information about messages
    :type chat_id: :class:`int`
    
    :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    
    :param from_message_id: The message identifier from which to return information about messages; use 0 to get results from the last message
    :type from_message_id: :class:`int`
    
    """

    ID: str = Field("getChatMessageCalendar", alias="@type")
    chat_id: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')
    from_message_id: int

    @staticmethod
    def read(q: dict) -> GetChatMessageCalendar:
        return GetChatMessageCalendar.construct(**q)
