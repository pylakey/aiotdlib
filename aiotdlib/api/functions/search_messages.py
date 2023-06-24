# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    ChatList,
    SearchMessagesFilter,
)


class SearchMessages(BaseObject):
    """
    Searches for messages in all chats except secret chats. Returns the results in reverse chronological order (i.e., in order of decreasing (date, chat_id, message_id)). For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

    :param query: Query to search for
    :type query: :class:`String`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    :param min_date: If not 0, the minimum date of the messages to return
    :type min_date: :class:`Int32`
    :param max_date: If not 0, the maximum date of the messages to return
    :type max_date: :class:`Int32`
    :param chat_list: Chat list in which to search messages; pass null to search in all chats regardless of their chat list. Only Main and Archive chat lists are supported, defaults to None
    :type chat_list: :class:`ChatList`, optional
    :param filter_: Additional filter for messages to search; pass null to search for all messages. Filters searchMessagesFilterMention, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, searchMessagesFilterFailedToSend, and searchMessagesFilterPinned are unsupported in this function, defaults to None
    :type filter_: :class:`SearchMessagesFilter`, optional
    """

    ID: typing.Literal["searchMessages"] = "searchMessages"
    query: String
    offset: String
    limit: Int32
    min_date: Int32 = 0
    max_date: Int32 = 0
    chat_list: typing.Optional[ChatList] = None
    filter_: typing.Optional[SearchMessagesFilter] = Field(None, alias="filter")
