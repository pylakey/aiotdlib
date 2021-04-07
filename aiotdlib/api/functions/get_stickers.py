# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetStickers(BaseObject):
    """
    Returns stickers from the installed sticker sets that correspond to a given emoji. If the emoji is not empty, favorite and recently used stickers may also be returned
    
    Params:
        emoji (:class:`str`)
            String representation of emoji. If empty, returns all known installed stickers
        
        limit (:class:`int`)
            The maximum number of stickers to be returned
        
    """

    ID: str = Field("getStickers", alias="@type")
    emoji: str
    limit: int

    @staticmethod
    def read(q: dict) -> GetStickers:
        return GetStickers.construct(**q)
