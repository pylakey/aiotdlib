# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .file import File
from .thumbnail_format import ThumbnailFormat
from ..base_object import BaseObject


class Thumbnail(BaseObject):
    """
    Represents a thumbnail
    
    Params:
        format (:class:`ThumbnailFormat`)
            Thumbnail format
        
        width (:class:`int`)
            Thumbnail width
        
        height (:class:`int`)
            Thumbnail height
        
        file (:class:`File`)
            The thumbnail
        
    """

    ID: str = Field("thumbnail", alias="@type")
    format: ThumbnailFormat
    width: int
    height: int
    file: File

    @staticmethod
    def read(q: dict) -> Thumbnail:
        return Thumbnail.construct(**q)
