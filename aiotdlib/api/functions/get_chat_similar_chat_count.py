# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetChatSimilarChatCount(BaseObject):
    """
    Returns approximate number of chats similar to the given chat

    :param chat_id: Identifier of the target chat; must be an identifier of a channel chat
    :type chat_id: :class:`Int53`
    :param return_local: Pass true to get the number of chats without sending network requests, or -1 if the number of chats is unknown locally
    :type return_local: :class:`Bool`
    """

    ID: typing.Literal["getChatSimilarChatCount"] = Field(
        "getChatSimilarChatCount", validation_alias="@type", alias="@type"
    )
    chat_id: Int53
    return_local: Bool = False
