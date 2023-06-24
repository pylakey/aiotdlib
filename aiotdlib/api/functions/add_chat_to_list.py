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


class AddChatToList(BaseObject):
    """
    Adds a chat to a chat list. A chat can't be simultaneously in Main and Archive chat lists, so it is automatically removed from another one if needed

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param chat_list: The chat list. Use getChatListsToAddChat to get suitable chat lists
    :type chat_list: :class:`ChatList`
    """

    ID: typing.Literal["addChatToList"] = "addChatToList"
    chat_id: Int53
    chat_list: ChatList
