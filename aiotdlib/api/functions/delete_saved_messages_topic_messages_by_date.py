# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteSavedMessagesTopicMessagesByDate(BaseObject):
    """
    Deletes all messages between the specified dates in a Saved Messages topic. Messages sent in the last 30 seconds will not be deleted

    :param saved_messages_topic_id: Identifier of Saved Messages topic which messages will be deleted
    :type saved_messages_topic_id: :class:`Int53`
    :param min_date: The minimum date of the messages to delete
    :type min_date: :class:`Int32`
    :param max_date: The maximum date of the messages to delete
    :type max_date: :class:`Int32`
    """

    ID: typing.Literal["deleteSavedMessagesTopicMessagesByDate"] = Field(
        "deleteSavedMessagesTopicMessagesByDate", validation_alias="@type", alias="@type"
    )
    saved_messages_topic_id: Int53
    min_date: Int32
    max_date: Int32
