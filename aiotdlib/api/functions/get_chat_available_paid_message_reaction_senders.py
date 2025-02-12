# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatAvailablePaidMessageReactionSenders(BaseObject):
    """
    Returns the list of message sender identifiers, which can be used to send a paid reaction in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatAvailablePaidMessageReactionSenders"] = Field(
        "getChatAvailablePaidMessageReactionSenders", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
