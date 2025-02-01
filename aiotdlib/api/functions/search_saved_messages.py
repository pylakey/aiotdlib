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
    ReactionType,
)


class SearchSavedMessages(BaseObject):
    """
    Searches for messages tagged by the given reaction and with the given words in the Saved Messages chat; for Telegram Premium users only. Returns the results in reverse chronological order, i.e. in order of decreasing message_id. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit

    :param query: Query to search for
    :type query: :class:`String`
    :param from_message_id: Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message
    :type from_message_id: :class:`Int53`
    :param offset: Specify 0 to get results from exactly the message from_message_id or a negative offset to get the specified message and some newer messages
    :type offset: :class:`Int32`
    :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    :param saved_messages_topic_id: If not 0, only messages in the specified Saved Messages topic will be considered; pass 0 to consider all messages
    :type saved_messages_topic_id: :class:`Int53`
    :param tag: Tag to search for; pass null to return all suitable messages, defaults to None
    :type tag: :class:`ReactionType`, optional
    """

    ID: typing.Literal["searchSavedMessages"] = Field("searchSavedMessages", validation_alias="@type", alias="@type")
    query: String
    from_message_id: Int53
    offset: Int32
    limit: Int32
    saved_messages_topic_id: Int53 = 0
    tag: typing.Optional[ReactionType] = None
