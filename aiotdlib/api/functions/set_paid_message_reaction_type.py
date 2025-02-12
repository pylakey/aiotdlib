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


class SetPaidMessageReactionType(BaseObject):
    """
    Changes type of paid message reaction of the current user on a message. The message must have paid reaction added by the current user

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    :param type_: New type of the paid reaction
    :type type_: :class:`PaidReactionType`
    """

    ID: typing.Literal["setPaidMessageReactionType"] = Field(
        "setPaidMessageReactionType", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
    type_: PaidReactionType = Field(..., alias="type")
