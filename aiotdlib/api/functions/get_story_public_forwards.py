# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStoryPublicForwards(BaseObject):
    """
    Returns forwards of a story as a message to public chats and reposts by public channels. Can be used only if the story is posted on behalf of the current user or story.can_get_statistics == true. For optimal performance, the number of returned messages and stories is chosen by TDLib

    :param story_sender_chat_id: The identifier of the sender of the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: The identifier of the story
    :type story_id: :class:`Int32`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of messages and stories to be returned; must be positive and can't be greater than 100. For optimal performance, the number of returned objects is chosen by TDLib and can be smaller than the specified limit
    :type limit: :class:`Int32`
    """

    ID: typing.Literal["getStoryPublicForwards"] = Field(
        "getStoryPublicForwards", validation_alias="@type", alias="@type"
    )
    story_sender_chat_id: Int53
    story_id: Int32
    offset: String
    limit: Int32
