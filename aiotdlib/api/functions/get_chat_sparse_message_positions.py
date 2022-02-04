# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import SearchMessagesFilter


class GetChatSparseMessagePositions(BaseObject):
    """
    Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database
    
    :param chat_id: Identifier of the chat in which to return information about message positions
    :type chat_id: :class:`int`
    
    :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    
    :param from_message_id: The message identifier from which to return information about message positions
    :type from_message_id: :class:`int`
    
    :param limit: The expected number of message positions to be returned; 50-2000. A smaller number of positions can be returned, if there are not enough appropriate messages
    :type limit: :class:`int`
    
    """

    ID: str = Field("getChatSparseMessagePositions", alias="@type")
    chat_id: int
    filter_: SearchMessagesFilter = Field(..., alias='filter')
    from_message_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetChatSparseMessagePositions:
        return GetChatSparseMessagePositions.construct(**q)
