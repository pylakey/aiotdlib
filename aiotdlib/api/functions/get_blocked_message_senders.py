# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetBlockedMessageSenders(BaseObject):
    """
    Returns users and chats that were blocked by the current user
    
    Params:
        offset (:class:`int`)
            Number of users and chats to skip in the result; must be non-negative
        
        limit (:class:`int`)
            The maximum number of users and chats to return; up to 100
        
    """

    ID: str = Field("getBlockedMessageSenders", alias="@type")
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetBlockedMessageSenders:
        return GetBlockedMessageSenders.construct(**q)
