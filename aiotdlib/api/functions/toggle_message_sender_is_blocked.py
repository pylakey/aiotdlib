# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class ToggleMessageSenderIsBlocked(BaseObject):
    """
    Changes the block state of a message sender. Currently, only users and supergroup chats can be blocked
    
    Params:
        sender (:class:`MessageSender`)
            Message Sender
        
        is_blocked (:class:`bool`)
            New value of is_blocked
        
    """

    ID: str = Field("toggleMessageSenderIsBlocked", alias="@type")
    sender: MessageSender
    is_blocked: bool

    @staticmethod
    def read(q: dict) -> ToggleMessageSenderIsBlocked:
        return ToggleMessageSenderIsBlocked.construct(**q)
