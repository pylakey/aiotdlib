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


class GetChatMessagePosition(BaseObject):
    """
    Returns approximate 1-based position of a message among messages, which can be found by the specified filter in the chat. Cannot be used in secret chats

    :param chat_id: Identifier of the chat in which to find message position
    :type chat_id: :class:`Int53`
    :param message_id: Message identifier
    :type message_id: :class:`Int53`
    :param filter_: Filter for message content; searchMessagesFilterEmpty, searchMessagesFilterUnreadMention, searchMessagesFilterUnreadReaction, and searchMessagesFilterFailedToSend are unsupported in this function
    :type filter_: :class:`SearchMessagesFilter`
    :param message_thread_id: If not 0, only messages in the specified thread will be considered; supergroups only
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["getChatMessagePosition"] = "getChatMessagePosition"
    chat_id: Int53
    message_id: Int53
    filter_: SearchMessagesFilter = Field(..., alias="filter")
    message_thread_id: Int53 = 0
