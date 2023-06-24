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


class RemoveMessageReaction(BaseObject):
    """
    Removes a reaction from a message. A chosen reaction can always be removed

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param reaction_type: Type of the reaction to remove
    :type reaction_type: :class:`ReactionType`
    """

    ID: typing.Literal["removeMessageReaction"] = "removeMessageReaction"
    chat_id: Int53
    message_id: Int53
    reaction_type: ReactionType
