# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class PhotoSize(BaseObject):
    """
    Describes an image in JPEG format
    
    Params:
        type_ (:class:`str`)
            Image type (see https://core.telegram.org/constructor/photoSize)
        
        photo (:class:`File`)
            Information about the image file
        
        width (:class:`int`)
            Image width
        
        height (:class:`int`)
            Image height
        
        progressive_sizes (:obj:`list[int]`)
            Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image
        
    """

    ID: str = Field("photoSize", alias="@type")
    type_: str = Field(..., alias='type')
    photo: File
    width: int
    height: int
    progressive_sizes: list[int]

    @staticmethod
    def read(q: dict) -> PhotoSize:
        return PhotoSize.construct(**q)
