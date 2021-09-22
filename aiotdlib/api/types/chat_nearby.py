# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ChatNearby(BaseObject):
    """
    Describes a chat located nearby
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param distance: Distance to the chat location, in meters
    :type distance: :class:`int`
    
    """

    ID: str = Field("chatNearby", alias="@type")
    chat_id: int
    distance: int

    @staticmethod
    def read(q: dict) -> ChatNearby:
        return ChatNearby.construct(**q)
