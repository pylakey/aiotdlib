# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetStickerSet(BaseObject):
    """
    Returns information about a sticker set by its identifier
    
    Params:
        set_id (:class:`int`)
            Identifier of the sticker set
        
    """

    ID: str = Field("getStickerSet", alias="@type")
    set_id: int

    @staticmethod
    def read(q: dict) -> GetStickerSet:
        return GetStickerSet.construct(**q)
