# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputSticker


class AddStickerToSet(BaseObject):
    """
    Adds a new sticker to a set; for bots only. Returns the sticker set
    
    Params:
        user_id (:class:`int`)
            Sticker set owner
        
        name (:class:`str`)
            Sticker set name
        
        sticker (:class:`InputSticker`)
            Sticker to add to the set
        
    """

    ID: str = Field("addStickerToSet", alias="@type")
    user_id: int
    name: str
    sticker: InputSticker

    @staticmethod
    def read(q: dict) -> AddStickerToSet:
        return AddStickerToSet.construct(**q)
