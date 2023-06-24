# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class DeleteChatMessagesByDate(BaseObject):
    """
    Deletes all messages between the specified dates in a chat. Supported only for private chats and basic groups. Messages sent in the last 30 seconds will not be deleted

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param min_date: The minimum date of the messages to delete
    :type min_date: :class:`Int32`
    :param max_date: The maximum date of the messages to delete
    :type max_date: :class:`Int32`
    :param revoke: Pass true to delete chat messages for all users; private chats only
    :type revoke: :class:`Bool`
    """

    ID: typing.Literal["deleteChatMessagesByDate"] = "deleteChatMessagesByDate"
    chat_id: Int53
    min_date: Int32
    max_date: Int32
    revoke: Bool = False
