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
    
    Params:
        has_stickers (:class:`bool`)
            True, if stickers were added to the photo. The list of corresponding sticker sets can be received using getAttachedStickerSets
        
        minithumbnail (:class:`Minithumbnail`)
            Photo minithumbnail; may be null
        
        sizes (:obj:`list[PhotoSize]`)
            Available variants of the photo, in different sizes
        
    """

    ID: str = Field("photo", alias="@type")
    has_stickers: bool
    minithumbnail: typing.Optional[Minithumbnail] = None
    sizes: list[PhotoSize]

    @staticmethod
    def read(q: dict) -> Photo:
        return Photo.construct(**q)
