# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import SearchMessagesFilter
from ..base_object import BaseObject


class SearchSecretMessages(BaseObject):
    """
    Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib
    
    :param chat_id: Identifier of the chat in which to search. Specify 0 to search in all secret chats
    :type chat_id: :class:`int`
    
    :param query: Query to search for. If empty, searchChatMessages should be used instead
    :type query: :class:`str`
    
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get first chunk of results
    :type offset: :class:`str`
    
    :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`int`
    
    :param filter_: A filter for message content in the search results
    :type filter_: :class:`SearchMessagesFilter`
    
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
