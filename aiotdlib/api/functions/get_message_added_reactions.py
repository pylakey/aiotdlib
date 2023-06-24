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


class GetMessageAddedReactions(BaseObject):
    """
    Returns reactions added for a message, along with their sender

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param offset: Offset of the first entry to return as received from the previous request; use empty string to get the first chunk of results
    :type offset: :class:`String`
    :param limit: The maximum number of reactions to be returned; must be positive and can't be greater than 100
    :type limit: :class:`Int32`
    :param reaction_type: Type of the reactions to return; pass null to return all added reactions, defaults to None
    :type reaction_type: :class:`ReactionType`, optional
    """

    ID: typing.Literal["getMessageAddedReactions"] = "getMessageAddedReactions"
    chat_id: Int53
    message_id: Int53
    offset: String
    limit: Int32
    reaction_type: typing.Optional[ReactionType] = None
