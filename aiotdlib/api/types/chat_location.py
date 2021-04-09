# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .location import Location
from ..base_object import BaseObject


class ChatLocation(BaseObject):
    """
    Represents a location to which a chat is connected
    
    Params:
        location (:class:`Location`)
            The location
        
        address (:class:`str`)
            Location address; 1-64 characters, as defined by the chat owner
        
    """

    ID: str = Field("chatLocation", alias="@type")
    location: Location
    address: str = Field(..., min_length=1, max_length=64)

    @staticmethod
    def read(q: dict) -> ChatLocation:
        return ChatLocation.construct(**q)
