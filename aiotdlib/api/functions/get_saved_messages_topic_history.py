# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetSavedMessagesTopicHistory(BaseObject):
    """
    Returns messages in a Saved Messages topic. The messages are returned in reverse chronological order (i.e., in order of decreasing message_id)

    :param saved_messages_topic_id: Identifier of Saved Messages topic which messages will be fetched
    :type saved_messages_topic_id: :class:`Int53`
    :param from_message_id: Identifier of the message starting from which messages must be fetched; use 0 to get results from the last message
    :type from_message_id: :class:`Int53`
    :param offset: Specify 0 to get results from exactly the message from_message_id or a negative offset up to 99 to get additionally some newer messages
    :type offset: :class:`Int32`
    :param limit: The maximum number of messages to be returned; must be positive and can't be greater than 100. If the offset is negative, the limit must be greater than or equal to -offset. For optimal performance, the number of returned messages is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getSavedMessagesTopicHistory"] = Field(
        "getSavedMessagesTopicHistory", validation_alias="@type", alias="@type"
    )
    saved_messages_topic_id: Int53
    from_message_id: Int53
    offset: Int32
    limit: Int32
