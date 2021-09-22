# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import MessageSender
from ..base_object import BaseObject


class ToggleMessageSenderIsBlocked(BaseObject):
    """
    Changes the block state of a message sender. Currently, only users and supergroup chats can be blocked
    
    :param sender: Message Sender
    :type sender: :class:`MessageSender`
    
    :param is_blocked: New value of is_blocked
    :type is_blocked: :class:`bool`
    
    """

    ID: str = Field("toggleMessageSenderIsBlocked", alias="@type")
    sender: MessageSender
    is_blocked: bool

    @staticmethod
    def read(q: dict) -> ToggleMessageSenderIsBlocked:
        return ToggleMessageSenderIsBlocked.construct(**q)
