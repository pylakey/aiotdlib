# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetInstalledStickerSets(BaseObject):
    """
    Returns a list of installed sticker sets
    
    Params:
        is_masks (:class:`bool`)
            Pass true to return mask sticker sets; pass false to return ordinary sticker sets
        
    """

    ID: str = Field("getInstalledStickerSets", alias="@type")
    is_masks: bool

    @staticmethod
    def read(q: dict) -> GetInstalledStickerSets:
        return GetInstalledStickerSets.construct(**q)
