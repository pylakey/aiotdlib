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


class ToggleMessageSenderIsBlocked(BaseObject):
    """
    Changes the block state of a message sender. Currently, only users and supergroup chats can be blocked

    :param sender_id: Identifier of a message sender to block/unblock
    :type sender_id: :class:`MessageSender`
    :param is_blocked: New value of is_blocked
    :type is_blocked: :class:`Bool`
    """

    ID: typing.Literal["toggleMessageSenderIsBlocked"] = "toggleMessageSenderIsBlocked"
    sender_id: MessageSender
    is_blocked: Bool
