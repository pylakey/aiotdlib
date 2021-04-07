# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .input_file import InputFile
from ..base_object import BaseObject


class InputThumbnail(BaseObject):
    """
    A thumbnail to be sent along with a file; must be in JPEG or WEBP format for stickers, and less than 200 KB in size
    
    Params:
        thumbnail (:class:`InputFile`)
            Thumbnail file to send. Sending thumbnails by file_id is currently not supported
        
        width (:class:`int`)
            Thumbnail width, usually shouldn't exceed 320. Use 0 if unknown
        
        height (:class:`int`)
            Thumbnail height, usually shouldn't exceed 320. Use 0 if unknown
        
    """

    ID: str = Field("inputThumbnail", alias="@type")
    thumbnail: InputFile
    width: int
    height: int

    @staticmethod
    def read(q: dict) -> InputThumbnail:
        return InputThumbnail.construct(**q)
