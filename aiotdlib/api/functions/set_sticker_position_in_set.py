# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class SetStickerPositionInSet(BaseObject):
    """
    Changes the position of a sticker in the set to which it belongs; for bots only. The sticker set must have been created by the bot
    
    Params:
        sticker (:class:`InputFile`)
            Sticker
        
        position (:class:`int`)
            New position of the sticker in the set, zero-based
        
    """

    ID: str = Field("setStickerPositionInSet", alias="@type")
    sticker: InputFile
    position: int

    @staticmethod
    def read(q: dict) -> SetStickerPositionInSet:
        return SetStickerPositionInSet.construct(**q)
