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


class SetPinnedChats(BaseObject):
    """
    Changes the order of pinned chats

    :param chat_list: Chat list in which to change the order of pinned chats
    :type chat_list: :class:`ChatList`
    :param chat_ids: The new list of pinned chats
    :type chat_ids: :class:`Vector[Int53]`
    """

    ID: typing.Literal["setPinnedChats"] = "setPinnedChats"
    chat_list: ChatList
    chat_ids: Vector[Int53]
