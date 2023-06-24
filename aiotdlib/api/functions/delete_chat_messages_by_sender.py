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
    MessageSender,
)


class DeleteChatMessagesBySender(BaseObject):
    """
    Deletes all messages sent by the specified message sender in a chat. Supported only for supergroups; requires can_delete_messages administrator privileges

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param sender_id: Identifier of the sender of messages to delete
    :type sender_id: :class:`MessageSender`
    """

    ID: typing.Literal["deleteChatMessagesBySender"] = "deleteChatMessagesBySender"
    chat_id: Int53
    sender_id: MessageSender
