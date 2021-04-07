# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetArchivedStickerSets(BaseObject):
    """
    Returns a list of archived sticker sets
    
    Params:
        is_masks (:class:`bool`)
            Pass true to return mask stickers sets; pass false to return ordinary sticker sets
        
        offset_sticker_set_id (:class:`int`)
            Identifier of the sticker set from which to return the result
        
        limit (:class:`int`)
            The maximum number of sticker sets to return
        
    """

    ID: str = Field("getArchivedStickerSets", alias="@type")
    is_masks: bool
    offset_sticker_set_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetArchivedStickerSets:
        return GetArchivedStickerSets.construct(**q)
