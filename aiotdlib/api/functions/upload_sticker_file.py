# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputSticker


class UploadStickerFile(BaseObject):
    """
    Uploads a PNG image with a sticker; returns the uploaded file
    
    Params:
        user_id (:class:`int`)
            Sticker file owner; ignored for regular users
        
        sticker (:class:`InputSticker`)
            Sticker file to upload
        
    """

    ID: str = Field("uploadStickerFile", alias="@type")
    user_id: int
    sticker: InputSticker

    @staticmethod
    def read(q: dict) -> UploadStickerFile:
        return UploadStickerFile.construct(**q)
