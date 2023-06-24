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
    ChatList,
)


class LoadChats(BaseObject):
    """
    Loads more chats from a chat list. The loaded chats and their positions in the chat list will be sent through updates. Chats are sorted by the pair (chat.position.order, chat.id) in descending order. Returns a 404 error if all chats have been loaded

    :param limit: The maximum number of chats to be loaded. For optimal performance, the number of loaded chats is chosen by TDLib and can be smaller than the specified limit, even if the end of the list is not reached
    :type limit: :class:`Int32`
    :param chat_list: The chat list in which to load chats; pass null to load chats from the main chat list, defaults to None
    :type chat_list: :class:`ChatList`, optional
    """

    ID: typing.Literal["loadChats"] = "loadChats"
    limit: Int32
    chat_list: typing.Optional[ChatList] = None
