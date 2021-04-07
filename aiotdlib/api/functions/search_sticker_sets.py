# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchStickerSets(BaseObject):
    """
    Searches for ordinary sticker sets by looking for specified query in their title and name. Excludes installed sticker sets from the results
    
    Params:
        query (:class:`str`)
            Query to search for
        
    """

    ID: str = Field("searchStickerSets", alias="@type")
    query: str

    @staticmethod
    def read(q: dict) -> SearchStickerSets:
        return SearchStickerSets.construct(**q)
