# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .minithumbnail import Minithumbnail
from .photo_size import PhotoSize
from ..base_object import BaseObject


class Photo(BaseObject):
    """
    Describes a photo
    
    :param has_stickers: True, if stickers were added to the photo. The list of corresponding sticker sets can be received using getAttachedStickerSets
    :type has_stickers: :class:`bool`
    
    :param minithumbnail: Photo minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param sizes: Available variants of the photo, in different sizes
    :type sizes: :class:`list[PhotoSize]`
    
    """

    ID: str = Field("photo", alias="@type")
    has_stickers: bool
    minithumbnail: typing.Optional[Minithumbnail] = None
    sizes: list[PhotoSize]

    @staticmethod
    def read(q: dict) -> Photo:
        return Photo.construct(**q)
