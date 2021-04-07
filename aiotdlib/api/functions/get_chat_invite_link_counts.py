# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetChatInviteLinkCounts(BaseObject):
    """
    Returns list of chat administrators with number of their invite links. Requires owner privileges in the chat
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
    """

    ID: str = Field("getChatInviteLinkCounts", alias="@type")
    chat_id: int

    @staticmethod
    def read(q: dict) -> GetChatInviteLinkCounts:
        return GetChatInviteLinkCounts.construct(**q)
