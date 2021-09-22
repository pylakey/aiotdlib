# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .chat_photo import ChatPhoto
from ..base_object import BaseObject


class ChatPhotos(BaseObject):
    """
    Contains a list of chat or user profile photos
    
    :param total_count: Total number of photos
    :type total_count: :class:`int`
    
    :param photos: List of photos
    :type photos: :class:`list[ChatPhoto]`
    
    """

    ID: str = Field("chatPhotos", alias="@type")
    total_count: int
    photos: list[ChatPhoto]

    @staticmethod
    def read(q: dict) -> ChatPhotos:
        return ChatPhotos.construct(**q)
