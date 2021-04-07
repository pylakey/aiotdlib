# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChatNearby(BaseObject):
    """
    Describes a chat located nearby
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        distance (:class:`int`)
            Distance to the chat location, in meters
        
    """

    ID: str = Field("chatNearby", alias="@type")
    chat_id: int
    distance: int

    @staticmethod
    def read(q: dict) -> ChatNearby:
        return ChatNearby.construct(**q)
