# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class UploadStickerFile(BaseObject):
    """
    Uploads a PNG image with a sticker; for bots only; returns the uploaded file
    
    Params:
        user_id (:class:`int`)
            Sticker file owner
        
        png_sticker (:class:`InputFile`)
            PNG image with the sticker; must be up to 512 KB in size and fit in 512x512 square
        
    """

    ID: str = Field("uploadStickerFile", alias="@type")
    user_id: int
    png_sticker: InputFile

    @staticmethod
    def read(q: dict) -> UploadStickerFile:
        return UploadStickerFile.construct(**q)
