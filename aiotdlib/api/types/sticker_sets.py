# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .sticker_set_info import StickerSetInfo
from ..base_object import BaseObject


class StickerSets(BaseObject):
    """
    Represents a list of sticker sets
    
    Params:
        total_count (:class:`int`)
            Approximate total number of sticker sets found
        
        sets (:obj:`list[StickerSetInfo]`)
            List of sticker sets
        
    """

    ID: str = Field("stickerSets", alias="@type")
    total_count: int
    sets: list[StickerSetInfo]

    @staticmethod
    def read(q: dict) -> StickerSets:
        return StickerSets.construct(**q)
