# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputFile
from ..base_object import BaseObject


class SetStickerSetThumbnail(BaseObject):
    """
    Sets a sticker set thumbnail; for bots only. Returns the sticker set
    
    :param user_id: Sticker set owner
    :type user_id: :class:`int`
    
    :param name: Sticker set name
    :type name: :class:`str`
    
    :param thumbnail: Thumbnail to set in PNG or TGS format. Animated thumbnail must be set for animated sticker sets and only for them. Pass a zero InputFileId to delete the thumbnail
    :type thumbnail: :class:`InputFile`
    
    """

    ID: str = Field("setStickerSetThumbnail", alias="@type")
    user_id: int
    name: str
    thumbnail: InputFile

    @staticmethod
    def read(q: dict) -> SetStickerSetThumbnail:
        return SetStickerSetThumbnail.construct(**q)
