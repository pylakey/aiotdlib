# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchInstalledStickerSets(BaseObject):
    """
    Searches for installed sticker sets by looking for specified query in their title and name
    
    Params:
        is_masks (:class:`bool`)
            Pass true to return mask sticker sets; pass false to return ordinary sticker sets
        
        query (:class:`str`)
            Query to search for
        
        limit (:class:`int`)
            The maximum number of sticker sets to return
        
    """

    ID: str = Field("searchInstalledStickerSets", alias="@type")
    is_masks: bool
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchInstalledStickerSets:
        return SearchInstalledStickerSets.construct(**q)
