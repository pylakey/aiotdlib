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


class ToggleChatIsPinned(BaseObject):
    """
    Changes the pinned state of a chat. There can be up to getOption("pinned_chat_count_max")/getOption("pinned_archived_chat_count_max") pinned non-secret chats and the same number of secret chats in the main/archive chat list. The limit can be increased with Telegram Premium

    :param chat_list: Chat list in which to change the pinned state of the chat
    :type chat_list: :class:`ChatList`
    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param is_pinned: Pass true to pin the chat; pass false to unpin it
    :type is_pinned: :class:`Bool`
    """

    ID: typing.Literal["toggleChatIsPinned"] = "toggleChatIsPinned"
    chat_list: ChatList
    chat_id: Int53
    is_pinned: Bool = False
