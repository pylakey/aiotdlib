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


class SetChatMessageSender(BaseObject):
    """
    Selects a message sender to send messages in a chat

    :param chat_id: Chat identifier
    :type chat_id: :class:`Int53`
    :param message_sender_id: New message sender for the chat
    :type message_sender_id: :class:`MessageSender`
    """

    ID: typing.Literal["setChatMessageSender"] = "setChatMessageSender"
    chat_id: Int53
    message_sender_id: MessageSender
