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


class SetStoryReaction(BaseObject):
    """
    Changes chosen reaction on a story

    :param story_sender_chat_id: The identifier of the sender of the story
    :type story_sender_chat_id: :class:`Int53`
    :param story_id: The identifier of the story
    :type story_id: :class:`Int32`
    :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions
    :type update_recent_reactions: :class:`Bool`
    :param reaction_type: Type of the reaction to set; pass null to remove the reaction. `reactionTypeCustomEmoji` reactions can be used only by Telegram Premium users, defaults to None
    :type reaction_type: :class:`ReactionType`, optional
    """

    ID: typing.Literal["setStoryReaction"] = "setStoryReaction"
    story_sender_chat_id: Int53
    story_id: Int32
    update_recent_reactions: Bool = False
    reaction_type: typing.Optional[ReactionType] = None
