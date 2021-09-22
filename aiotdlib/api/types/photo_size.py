# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class PhotoSize(BaseObject):
    """
    Describes an image in JPEG format
    
    :param type_: Image type (see https://core.telegram.org/constructor/photoSize)
    :type type_: :class:`str`
    
    :param photo: Information about the image file
    :type photo: :class:`File`
    
    :param width: Image width
    :type width: :class:`int`
    
    :param height: Image height
    :type height: :class:`int`
    
    :param progressive_sizes: Sizes of progressive JPEG file prefixes, which can be used to preliminarily show the image; in bytes
    :type progressive_sizes: :class:`list[int]`
    
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
