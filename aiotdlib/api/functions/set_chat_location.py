# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatLocation


class SetChatLocation(BaseObject):
    """
    Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use
    
    Params:
        chat_id (:class:`int`)
            Chat identifier
        
        location (:class:`ChatLocation`)
            New location for the chat; must be valid and not null
        
    """

    ID: str = Field("setChatLocation", alias="@type")
    chat_id: int
    location: ChatLocation

    @staticmethod
    def read(q: dict) -> SetChatLocation:
        return SetChatLocation.construct(**q)
