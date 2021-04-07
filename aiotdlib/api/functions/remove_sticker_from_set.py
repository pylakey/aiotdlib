# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class RemoveStickerFromSet(BaseObject):
    """
    Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot
    
    Params:
        sticker (:class:`InputFile`)
            Sticker
        
    """

    ID: str = Field("removeStickerFromSet", alias="@type")
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> RemoveStickerFromSet:
        return RemoveStickerFromSet.construct(**q)
