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
    MessageSender,
    SearchMessagesFilter,
)


class SearchChatMessages(BaseObject):
    """
    Searches for messages with given words in the chat. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. Cannot be used in secret chats with a non-empty query (searchSecretMessages must be used instead), or without an enabled message database. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit. A combination of query, sender_id, filter and message_thread_id search criteria is expected to be supported, only if it is required for Telegram official application implementation

    :param chat_id: Identifier of the chat in which to search messages
    :type chat_id: :class:`Int53`
    :param query: Query to search for
    :type query: :class:`String`
    :param from_message_id: Identifier of the message starting from which history must be fetched; use 0 to get results from the last message
    :type from_message_id: :class:`Int53`
    :param offset: Specify 0 to get results from exactly the from_message_id or a negative offset to get the specified message and some newer messages
    :type offset: :class:`Int32`
    :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    :param message_thread_id: If not 0, only messages in the specified thread will be returned; supergroups only
    :type message_thread_id: :class:`Int53`
    :param sender_id: Identifier of the sender of messages to search for; pass null to search for messages from any sender. Not supported in secret chats, defaults to None
    :type sender_id: :class:`MessageSender`, optional
    :param filter_: Additional filter for messages to search; pass null to search for all messages, defaults to None
    :type filter_: :class:`SearchMessagesFilter`, optional
    """

    ID: typing.Literal["searchChatMessages"] = "searchChatMessages"
    chat_id: Int53
    query: String
    from_message_id: Int53
    offset: Int32
    limit: Int32
    message_thread_id: Int53 = 0
    sender_id: typing.Optional[MessageSender] = None
    filter_: typing.Optional[SearchMessagesFilter] = Field(None, alias="filter")
