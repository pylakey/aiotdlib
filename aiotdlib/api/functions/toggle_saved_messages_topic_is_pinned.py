# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleSavedMessagesTopicIsPinned(BaseObject):
    """
    Changes the pinned state of a Saved Messages topic. There can be up to getOption("pinned_saved_messages_topic_count_max") pinned topics. The limit can be increased with Telegram Premium

    :param saved_messages_topic_id: Identifier of Saved Messages topic to pin or unpin
    :type saved_messages_topic_id: :class:`Int53`
    :param is_pinned: Pass true to pin the topic; pass false to unpin it
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["toggleSavedMessagesTopicIsPinned"] = Field(
        "toggleSavedMessagesTopicIsPinned", validation_alias="@type", alias="@type"
    )
    saved_messages_topic_id: Int53
    is_pinned: Bool = False
