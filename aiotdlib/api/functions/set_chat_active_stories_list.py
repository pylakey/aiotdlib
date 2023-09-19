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
    StoryList,
)


class SetChatActiveStoriesList(BaseObject):
    """
    Changes story list in which stories from the chat are shown

    :param chat_id: Identifier of the chat that posted stories
    :type chat_id: :class:`Int53`
    :param story_list: New list for active stories posted by the chat
    :type story_list: :class:`StoryList`
    """

    ID: typing.Literal["setChatActiveStoriesList"] = "setChatActiveStoriesList"
    chat_id: Int53
    story_list: StoryList
