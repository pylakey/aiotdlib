# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatSimilarChats(BaseObject):
    """
    Returns a list of chats similar to the given chat

    :param chat_id: Identifier of the target chat; must be an identifier of a channel chat
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["getChatSimilarChats"] = Field("getChatSimilarChats", validation_alias="@type", alias="@type")
    chat_id: Int53
