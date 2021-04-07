# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchStickers(BaseObject):
    """
    Searches for stickers from public sticker sets that correspond to a given emoji
    
    Params:
        emoji (:class:`str`)
            String representation of emoji; must be non-empty
        
        limit (:class:`int`)
            The maximum number of stickers to be returned
        
    """

    ID: str = Field("searchStickers", alias="@type")
    emoji: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchStickers:
        return SearchStickers.construct(**q)
