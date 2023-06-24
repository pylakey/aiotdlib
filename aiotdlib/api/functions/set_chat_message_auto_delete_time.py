# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SetChatMessageAutoDeleteTime(BaseObject):
    """
    Changes the message auto-delete or self-destruct (for secret chats) time in a chat. Requires change_info administrator right in basic groups, supergroups and channels Message auto-delete time can't be changed in a chat with the current user (Saved Messages) and the chat 777000 (Telegram).

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_auto_delete_time: New time value, in seconds; unless the chat is secret, it must be from 0 up to 365 * 86400 and be divisible by 86400. If 0, then messages aren't deleted automatically
    :type message_auto_delete_time: :class:`Int32`
    """

    ID: typing.Literal["setChatMessageAutoDeleteTime"] = "setChatMessageAutoDeleteTime"
    chat_id: Int53
    message_auto_delete_time: Int32 = 0
