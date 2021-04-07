# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .chat_photo import ChatPhoto
from ..base_object import BaseObject


class ChatPhotos(BaseObject):
    """
    Contains a list of chat or user profile photos
    
    Params:
        total_count (:class:`int`)
            Total number of photos
        
        photos (:obj:`list[ChatPhoto]`)
            List of photos
        
    """

    ID: str = Field("chatPhotos", alias="@type")
    total_count: int
    photos: list[ChatPhoto]

    @staticmethod
    def read(q: dict) -> ChatPhotos:
        return ChatPhotos.construct(**q)
