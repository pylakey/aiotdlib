# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class SetStickerSetThumbnail(BaseObject):
    """
    Sets a sticker set thumbnail; for bots only. Returns the sticker set
    
    Params:
        user_id (:class:`int`)
            Sticker set owner
        
        name (:class:`str`)
            Sticker set name
        
        thumbnail (:class:`InputFile`)
            Thumbnail to set in PNG or TGS format. Animated thumbnail must be set for animated sticker sets and only for them. Pass a zero InputFileId to delete the thumbnail
        
    """

    ID: str = Field("setStickerSetThumbnail", alias="@type")
    user_id: int
    name: str
    thumbnail: InputFile

    @staticmethod
    def read(q: dict) -> SetStickerSetThumbnail:
        return SetStickerSetThumbnail.construct(**q)
