# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class UnpinAllMessageThreadMessages(BaseObject):
    """
    Removes all pinned messages from a forum topic; requires can_pin_messages rights in the supergroup

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_thread_id: Message thread identifier in which messages will be unpinned
    :type message_thread_id: :class:`Int53`
    """

    ID: typing.Literal["unpinAllMessageThreadMessages"] = "unpinAllMessageThreadMessages"
    chat_id: Int53
    message_thread_id: Int53
