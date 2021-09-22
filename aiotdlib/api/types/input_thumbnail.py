# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .input_file import InputFile
from ..base_object import BaseObject


class InputThumbnail(BaseObject):
    """
    A thumbnail to be sent along with a file; must be in JPEG or WEBP format for stickers, and less than 200 KB in size
    
    :param thumbnail: Thumbnail file to send. Sending thumbnails by file_id is currently not supported
    :type thumbnail: :class:`InputFile`
    
    :param width: Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown
    :type width: :class:`int`
    
    :param height: Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown
    :type height: :class:`int`
    
    """

    ID: str = Field("inputThumbnail", alias="@type")
    thumbnail: InputFile
    width: int
    height: int

    @staticmethod
    def read(q: dict) -> InputThumbnail:
        return InputThumbnail.construct(**q)
