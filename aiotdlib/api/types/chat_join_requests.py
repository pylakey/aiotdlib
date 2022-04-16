# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_join_request import ChatJoinRequest
from ..base_object import BaseObject


class ChatJoinRequests(BaseObject):
    """
    Contains a list of requests to join a chat
    
    :param total_count: Approximate total number of requests found
    :type total_count: :class:`int`
    
    :param requests: List of the requests
    :type requests: :class:`list[ChatJoinRequest]`
    
    """

    ID: str = Field("chatJoinRequests", alias="@type")
    total_count: int
    requests: list[ChatJoinRequest]

    @staticmethod
    def read(q: dict) -> ChatJoinRequests:
        return ChatJoinRequests.construct(**q)
