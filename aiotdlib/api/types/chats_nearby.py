# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_nearby import ChatNearby
from ..base_object import BaseObject


class ChatsNearby(BaseObject):
    """
    Represents a list of chats located nearby
    
    :param users_nearby: List of users nearby
    :type users_nearby: :class:`list[ChatNearby]`
    
    :param supergroups_nearby: List of location-based supergroups nearby
    :type supergroups_nearby: :class:`list[ChatNearby]`
    
    """

    ID: str = Field("chatsNearby", alias="@type")
    users_nearby: list[ChatNearby]
    supergroups_nearby: list[ChatNearby]

    @staticmethod
    def read(q: dict) -> ChatsNearby:
        return ChatsNearby.construct(**q)
