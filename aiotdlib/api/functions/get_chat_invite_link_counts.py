# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetChatInviteLinkCounts(BaseObject):
    """
    Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    """

    ID: str = Field("getChatInviteLinkCounts", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatInviteLinkCounts:
        return GetChatInviteLinkCounts.construct(**q)
