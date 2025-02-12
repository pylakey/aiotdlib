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
    PaidReactionType,
)


class AddPendingPaidMessageReaction(BaseObject):
    """
    Adds the paid message reaction to a message. Use getMessageAvailableReactions to check whether the reaction is available for the message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param star_count: Number of Telegram Stars to be used for the reaction. The total number of pending paid reactions must not exceed getOption("paid_reaction_star_count_max")
    :type star_count: :class:`Int53`
    :param type_: Type of the paid reaction; pass null if the user didn't choose reaction type explicitly, for example, the reaction is set from the message bubble, defaults to None
    :type type_: :class:`PaidReactionType`, optional
    """

    ID: typing.Literal["addPendingPaidMessageReaction"] = Field(
        "addPendingPaidMessageReaction", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    star_count: Int53
    type_: typing.Optional[PaidReactionType] = Field(None, alias="type")
