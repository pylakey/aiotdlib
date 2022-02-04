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
    
    :param user_id: Sticker set owner
    :type user_id: :class:`int`
    
    :param name: Sticker set name
    :type name: :class:`str`
    
    :param thumbnail: Thumbnail to set in PNG, TGS, or WEBM format; pass null to remove the sticker set thumbnail. Thumbnail format must match the format of stickers in the set
    :type thumbnail: :class:`InputFile`
    
    """

    ID: str = Field("setStickerSetThumbnail", alias="@type")
    user_id: int
    name: str
    thumbnail: InputFile

    @staticmethod
    def read(q: dict) -> SetStickerSetThumbnail:
        return SetStickerSetThumbnail.construct(**q)
