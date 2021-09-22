# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .sticker_set_info import StickerSetInfo
from ..base_object import BaseObject


class StickerSets(BaseObject):
    """
    Represents a list of sticker sets
    
    :param total_count: Approximate total number of sticker sets found
    :type total_count: :class:`int`
    
    :param sets: List of sticker sets
    :type sets: :class:`list[StickerSetInfo]`
    
    """

    ID: str = Field("stickerSets", alias="@type")
    total_count: int
    sets: list[StickerSetInfo]

    @staticmethod
    def read(q: dict) -> StickerSets:
        return StickerSets.construct(**q)
