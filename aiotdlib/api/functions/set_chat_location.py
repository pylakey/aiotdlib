# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ChatLocation
from ..base_object import BaseObject


class SetChatLocation(BaseObject):
    """
    Changes the location of a chat. Available only for some location-based supergroups, use supergroupFullInfo.can_set_location to check whether the method is allowed to use
    
    :param chat_id: Chat identifier
    :type chat_id: :class:`int`
    
    :param location: New location for the chat; must be valid and not null
    :type location: :class:`ChatLocation`
    
    """

    ID: str = Field("setChatLocation", alias="@type")
    chat_id: int
    location: ChatLocation

    @staticmethod
    def read(q: dict) -> SetChatLocation:
        return SetChatLocation.construct(**q)
