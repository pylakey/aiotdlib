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


class AddMessageReaction(BaseObject):
    """
    Adds a reaction to a message. Use getMessageAvailableReactions to receive the list of available reactions for the message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param reaction_type: Type of the reaction to add
    :type reaction_type: :class:`ReactionType`
    :param is_big: Pass true if the reaction is added with a big animation
    :type is_big: :class:`Bool`
    :param update_recent_reactions: Pass true if the reaction needs to be added to recent reactions
    :type update_recent_reactions: :class:`Bool`
    """

    ID: typing.Literal["addMessageReaction"] = "addMessageReaction"
    chat_id: Int53
    message_id: Int53
    reaction_type: ReactionType
    is_big: Bool = False
    update_recent_reactions: Bool = False
