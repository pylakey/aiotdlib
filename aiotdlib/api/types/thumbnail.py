# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from .thumbnail_format import ThumbnailFormat
from ..base_object import BaseObject


class Thumbnail(BaseObject):
    """
    Represents a thumbnail
    
    :param format: Thumbnail format
    :type format: :class:`ThumbnailFormat`
    
    :param width: Thumbnail width
    :type width: :class:`int`
    
    :param height: Thumbnail height
    :type height: :class:`int`
    
    :param file: The thumbnail
    :type file: :class:`File`
    
    """

    ID: str = Field("thumbnail", alias="@type")
    format: ThumbnailFormat
    width: int
    height: int
    file: File

    @staticmethod
    def read(q: dict) -> Thumbnail:
        return Thumbnail.construct(**q)
