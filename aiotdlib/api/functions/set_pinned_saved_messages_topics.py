# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetPinnedSavedMessagesTopics(BaseObject):
    """
    Changes the order of pinned Saved Messages topics

    :param saved_messages_topic_ids: Identifiers of the new pinned Saved Messages topics
    :type saved_messages_topic_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["setPinnedSavedMessagesTopics"] = Field(
        "setPinnedSavedMessagesTopics", validation_alias="@type", alias="@type"
    )
    saved_messages_topic_ids: Vector[Int53]
