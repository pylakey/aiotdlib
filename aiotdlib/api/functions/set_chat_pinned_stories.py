# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatPinnedStories(BaseObject):
    """
    Changes the list of pinned stories on a chat page; requires can_edit_stories right in the chat

    :param chat_id: Identifier of the chat that posted the stories
    :type chat_id: :class:`Int53`
    :param story_ids: New list of pinned stories. All stories must be posted to the chat page first. There can be up to getOption("pinned_story_count_max") pinned stories on a chat page
    :type story_ids: :class:`Vector[Int32]`
    """

    ID: typing.Literal["setChatPinnedStories"] = Field("setChatPinnedStories", validation_alias="@type", alias="@type")
    chat_id: Int53
    story_ids: Vector[Int32]
