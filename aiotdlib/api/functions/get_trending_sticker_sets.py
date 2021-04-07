# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetTrendingStickerSets(BaseObject):
    """
    Returns a list of trending sticker sets. For the optimal performance the number of returned sticker sets is chosen by the library
    
    Params:
        offset (:class:`int`)
            The offset from which to return the sticker sets; must be non-negative
        
        limit (:class:`int`)
            The maximum number of sticker sets to be returned; must be non-negative. Fewer sticker sets may be returned than specified by the limit, even if the end of the list has not been reached
        
    """

    ID: str = Field("getTrendingStickerSets", alias="@type")
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetTrendingStickerSets:
        return GetTrendingStickerSets.construct(**q)
