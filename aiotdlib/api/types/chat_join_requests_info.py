# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatJoinRequestsInfo(BaseObject):
    """
    Contains information about pending join requests for a chat
    
    :param total_count: Total number of pending join requests
    :type total_count: :class:`int`
    
    :param user_ids: Identifiers of at most 3 users sent the newest pending join requests
    :type user_ids: :class:`list[int]`
    
    """

    ID: str = Field("chatJoinRequestsInfo", alias="@type")
    total_count: int
    user_ids: list[int]

    @staticmethod
    def read(q: dict) -> ChatJoinRequestsInfo:
        return ChatJoinRequestsInfo.construct(**q)
