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


class GetChatSparseMessagePositions(BaseObject):
    """
    Returns sparse positions of messages of the specified type in the chat to be used for shared media scroll implementation. Returns the results in reverse chronological order (i.e., in order of decreasing message_id). Cannot be used in secret chats or with searchMessagesFilterFailedToSend filter without an enabled message database

    :param chat_id: Identifier of the chat in which to return information about message positions
    :type chat_id: :class:`Int53`
    :param filter_: Filter for message content. Filters searchMessagesFilterEmpty, searchMessagesFilterMention, searchMessagesFilterUnreadMention, and searchMessagesFilterUnreadReaction are unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    :param from_message_id: The message identifier from which to return information about message positions
    :type from_message_id: :class:`Int53`
    :param limit: The expected number of message positions to be returned; 50-2000. A smaller number of positions can be returned, if there are not enough appropriate messages
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getChatSparseMessagePositions"] = "getChatSparseMessagePositions"
    chat_id: Int53
    filter_: SearchMessagesFilter = Field(..., alias="filter")
    from_message_id: Int53
    limit: Int32
