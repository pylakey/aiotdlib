# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class UnpinChatMessage(BaseObject):
    """
    Removes a pinned message from a chat; requires can_pin_messages rights in the group or can_edit_messages rights in the channel

    :param chat_id: Identifier of the chat
    :type chat_id: :class:`Int53`
    :param message_id: Identifier of the removed pinned message
    :type message_id: :class:`Int53`
    """

    ID: typing.Literal["unpinChatMessage"] = "unpinChatMessage"
    chat_id: Int53
    message_id: Int53
