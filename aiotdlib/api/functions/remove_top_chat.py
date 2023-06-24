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
    TopChatCategory,
)


class RemoveTopChat(BaseObject):
    """
    Removes a chat from the list of frequently used chats. Supported only if the chat info database is enabled

    :param category: Category of frequently used chats
    :type category: :class:`TopChatCategory`
    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    """

    ID: typing.Literal["removeTopChat"] = "removeTopChat"
    category: TopChatCategory
    chat_id: Int53
