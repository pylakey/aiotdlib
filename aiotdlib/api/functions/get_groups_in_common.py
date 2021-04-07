# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetGroupsInCommon(BaseObject):
    """
    Returns a list of common group chats with a given user. Chats are sorted by their type and creation date
    
    Params:
        user_id (:class:`int`)
            User identifier
        
        offset_chat_id (:class:`int`)
            Chat identifier starting from which to return chats; use 0 for the first request
        
        limit (:class:`int`)
            The maximum number of chats to be returned; up to 100
        
    """

    ID: str = Field("getGroupsInCommon", alias="@type")
    user_id: int
    offset_chat_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetGroupsInCommon:
        return GetGroupsInCommon.construct(**q)
