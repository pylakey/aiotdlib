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
    SearchMessagesFilter,
)


class SearchSecretMessages(BaseObject):
    """
    Searches for messages in secret chats. Returns the results in reverse chronological order. For optimal performance, the number of returned messages is chosen by TDLib

    :param chat_id: Identifier of the chat in which to search. Specify 0 to search in all secret chats
    :type chat_id: :class:`Int53`
    :param query: Query to search for. If empty, searchChatMessages must be used instead
    :type query: :class:`String`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of messages to be returned; up to 100. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    :param filter_: Additional filter for messages to search; pass null to search for all messages, defaults to None
    :type filter_: :class:`SearchMessagesFilter`, optional
    """

    ID: typing.Literal["searchSecretMessages"] = "searchSecretMessages"
    chat_id: Int53
    query: String
    offset: String
    limit: Int32
    filter_: typing.Optional[SearchMessagesFilter] = Field(None, alias="filter")
