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


class GetChatStoryInteractions(BaseObject):
    """
    Returns interactions with a story posted in a chat. Can be used only if story is posted on behalf of a chat and the user is an administrator in the chat

    :param story_sender_chat_id: The identifier of the sender of the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: Story identifier
    :type story_id: :class:`Int32`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of story interactions to return
    :type limit: :class:`Int32`
    :param prefer_forwards: Pass true to get forwards and reposts first, then reactions, then other views; pass false to get interactions sorted just by interaction date
    :type prefer_forwards: :class:`Bool`
    :param reaction_type: Pass the default heart reaction or a suggested reaction type to receive only interactions with the specified reaction type; pass null to receive all interactions; reactionTypePaid isn't supported, defaults to None
    :type reaction_type: :class:`ReactionType`, optional
    """

    ID: typing.Literal["getChatStoryInteractions"] = Field(
        "getChatStoryInteractions", validation_alias="@type", alias="@type"
    )
    story_sender_chat_id: Int53
    story_id: Int32
    offset: String
    limit: Int32
    prefer_forwards: Bool = False
    reaction_type: typing.Optional[ReactionType] = None
