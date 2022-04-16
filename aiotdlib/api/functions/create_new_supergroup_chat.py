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
    
    :param title: Title of the new chat; 1-128 characters
    :type title: :class:`str`
    
    :param is_channel: Pass true to create a channel chat
    :type is_channel: :class:`bool`
    
    :param param_description: Chat description; 0-255 characters, defaults to None
    :type param_description: :class:`str`, optional
    
    :param location: Chat location if a location-based supergroup is being created; pass null to create an ordinary supergroup chat
    :type location: :class:`ChatLocation`
    
    :param for_import: Pass true to create a supergroup for importing messages using importMessage
    :type for_import: :class:`bool`
    
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
