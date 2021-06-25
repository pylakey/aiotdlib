# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSuggestedStickerSetName(BaseObject):
    """
    Returns a suggested name for a new sticker set with a given title
    
    Params:
        title (:class:`str`)
            Sticker set title; 1-64 characters
        
    """

    ID: str = Field("getSuggestedStickerSetName", alias="@type")
    title: str = Field(..., min_length=1, max_length=64)

    @staticmethod
    def read(q: dict) -> GetSuggestedStickerSetName:
        return GetSuggestedStickerSetName.construct(**q)
