# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleChatViewAsTopics(BaseObject):
    """
    Changes the view_as_topics setting of a forum chat or Saved Messages

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param view_as_topics: New value of view_as_topics
    :type view_as_topics: :class:`Bool`
    """

    ID: typing.Literal["toggleChatViewAsTopics"] = Field(
        "toggleChatViewAsTopics", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    view_as_topics: Bool
