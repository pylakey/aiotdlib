# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteSavedMessagesTopicHistory(BaseObject):
    """
    Deletes all messages in a Saved Messages topic

    :param saved_messages_topic_id: Identifier of Saved Messages topic which messages will be deleted
    :type saved_messages_topic_id: :class:`Int53`
    """

    ID: typing.Literal["deleteSavedMessagesTopicHistory"] = Field(
        "deleteSavedMessagesTopicHistory", validation_alias="@type", alias="@type"
    )
    saved_messages_topic_id: Int53
