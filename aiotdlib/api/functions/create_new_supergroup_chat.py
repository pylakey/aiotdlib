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


class CreateNewSupergroupChat(BaseObject):
    """
    Creates a new supergroup or channel and sends a corresponding messageSupergroupChatCreate. Returns the newly created chat
    
    :param title: Title of the new chat; 1-128 characters
    :type title: :class:`str`
    
    :param is_channel: True, if a channel chat needs to be created
    :type is_channel: :class:`bool`
    
    :param param_description: Chat description; 0-255 characters, defaults to None
    :type param_description: :class:`str`, optional
    
    :param location: Chat location if a location-based supergroup is being created
    :type location: :class:`ChatLocation`
    
    :param for_import: True, if the supergroup is created for importing messages using importMessage
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
