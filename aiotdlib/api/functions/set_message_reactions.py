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


class SetMessageReactions(BaseObject):
    """
    Sets reactions on a message; for bots only

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param reaction_types: Types of the reaction to set; pass an empty list to remove the reactions
    :type reaction_types: :class:`Vector[ReactionType]`
    :param is_big: Pass true if the reactions are added with a big animation
    :type is_big: :class:`Bool`
    """

    ID: typing.Literal["setMessageReactions"] = Field("setMessageReactions", validation_alias="@type", alias="@type")
    chat_id: Int53
    message_id: Int53
    reaction_types: Vector[ReactionType]
    is_big: Bool = False
