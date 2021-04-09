# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject
from ..types import ChatLocation


class CreateNewSupergroupChat(BaseObject):
    """
    Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat
    
    Params:
        title (:class:`str`)
            Title of the new chat; 1-128 characters
        
        is_channel (:class:`bool`)
            True, if a channel chat needs to be created
        
        param_description (:class:`str`)
            Chat description; 0-255 characters
        
        location (:class:`ChatLocation`)
            Chat location if a location-based supergroup is being created
        
        for_import (:class:`bool`)
            True, if the supergroup is created for importing messages using importMessage
        
    """

    ID: str = Field("createNewSupergroupChat", alias="@type")
    title: str = Field(..., min_length=1, max_length=128)
    is_channel: bool
    param_description: typing.Optional[str] = Field(None, max_length=255)
    location: ChatLocation
    for_import: bool

    @staticmethod
    def read(q: dict) -> CreateNewSupergroupChat:
        return CreateNewSupergroupChat.construct(**q)
