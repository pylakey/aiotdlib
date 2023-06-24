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


class ReadChatList(BaseObject):
    """
    Traverse all chats in a chat list and marks all messages in the chats as read

    :param chat_list: Chat list in which to mark all chats as read
    :type chat_list: :class:`ChatList`
    """

    ID: typing.Literal["readChatList"] = "readChatList"
    chat_list: ChatList
