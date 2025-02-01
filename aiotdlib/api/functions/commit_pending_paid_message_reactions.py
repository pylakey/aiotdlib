# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CommitPendingPaidMessageReactions(BaseObject):
    """
    Applies all pending paid reactions on a message

    :param chat_id: Identifier of the chat to which the message belongs
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["commitPendingPaidMessageReactions"] = Field(
        "commitPendingPaidMessageReactions", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    message_id: Int53
