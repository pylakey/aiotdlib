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
    SearchMessagesFilter,
)


class GetChatMessageCount(BaseObject):
    """
    Returns approximate number of messages of the specified type in the chat

    :param chat_id: Identifier of the chat in which to count messages
    :type chat_id: :class:`Int53`
    :param filter_: Filter for message content; searchMessagesFilterEmpty is unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    :param return_local: Pass true to get the number of messages without sending network requests, or -1 if the number of messages is unknown locally
    :type return_local: :class:`Bool`
    """

    ID: typing.Literal["getChatMessageCount"] = "getChatMessageCount"
    chat_id: Int53
    filter_: SearchMessagesFilter = Field(..., alias="filter")
    return_local: Bool = False
