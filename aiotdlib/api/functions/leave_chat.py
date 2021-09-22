# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class LeaveChat(BaseObject):
    """
    Removes the current user from chat members. Private and secret chats can't be left using this method
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("leaveChat", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> LeaveChat:
        return LeaveChat.construct(**q)
