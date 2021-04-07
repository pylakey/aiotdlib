# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_nearby import ChatNearby
from ..base_object import BaseObject


class ChatsNearby(BaseObject):
    """
    Represents a list of chats located nearby
    
    Params:
        users_nearby (:obj:`list[ChatNearby]`)
            List of users nearby
        
        supergroups_nearby (:obj:`list[ChatNearby]`)
            List of location-based supergroups nearby
        
    """

    ID: str = Field("chatsNearby", alias="@type")
    users_nearby: list[ChatNearby]
    supergroups_nearby: list[ChatNearby]

    @staticmethod
    def read(q: dict) -> ChatsNearby:
        return ChatsNearby.construct(**q)
