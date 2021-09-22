# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .animated_chat_photo import AnimatedChatPhoto
from .minithumbnail import Minithumbnail
from .photo_size import PhotoSize
from ..base_object import BaseObject


class ChatPhoto(BaseObject):
    """
    Describes a chat or user profile photo
    
    :param id: Unique photo identifier
    :type id: :class:`int`
    
    :param added_date: Point in time (Unix timestamp) when the photo has been added
    :type added_date: :class:`int`
    
    :param minithumbnail: Photo minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param sizes: Available variants of the photo in JPEG format, in different size
    :type sizes: :class:`list[PhotoSize]`
    
    :param animation: Animated variant of the photo in MPEG4 format; may be null, defaults to None
    :type animation: :class:`AnimatedChatPhoto`, optional
    
    """

    ID: str = Field("chatPhoto", alias="@type")
    id: int
    added_date: int
    minithumbnail: typing.Optional[Minithumbnail] = None
    sizes: list[PhotoSize]
    animation: typing.Optional[AnimatedChatPhoto] = None

    @staticmethod
    def read(q: dict) -> ChatPhoto:
        return ChatPhoto.construct(**q)
