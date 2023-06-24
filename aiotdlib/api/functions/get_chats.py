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


class GetChats(BaseObject):
    """
    Returns an ordered list of chats from the beginning of a chat list. For informational purposes only. Use loadChats and updates processing instead to maintain chat lists in a consistent state

    :param limit: The maximum number of chats to be returned
    :type limit: :class:`Int32`
    :param chat_list: The chat list in which to return chats; pass null to get chats from the main chat list, defaults to None
    :type chat_list: :class:`ChatList`, optional
    """

    ID: typing.Literal["getChats"] = "getChats"
    limit: Int32
    chat_list: typing.Optional[ChatList] = None
