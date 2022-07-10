# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .sticker_set_info import StickerSetInfo
from ..base_object import BaseObject


class TrendingStickerSets(BaseObject):
    """
    Represents a list of trending sticker sets
    
    :param total_count: Approximate total number of trending sticker sets
    :type total_count: :class:`int`
    
    :param sets: List of trending sticker sets
    :type sets: :class:`list[StickerSetInfo]`
    
    :param is_premium: True, if the list contains sticker sets with premium stickers
    :type is_premium: :class:`bool`
    
    """

    ID: str = Field("trendingStickerSets", alias="@type")
    total_count: int
    sets: list[StickerSetInfo]
    is_premium: bool

    @staticmethod
    def read(q: dict) -> TrendingStickerSets:
        return TrendingStickerSets.construct(**q)
