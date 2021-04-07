# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchStickerSet(BaseObject):
    """
    Searches for a sticker set by its name
    
    Params:
        name (:class:`str`)
            Name of the sticker set
        
    """

    ID: str = Field("searchStickerSet", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> SearchStickerSet:
        return SearchStickerSet.construct(**q)
