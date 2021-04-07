# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class AddFavoriteSticker(BaseObject):
    """
    Adds a new sticker to the list of favorite stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list
    
    Params:
        sticker (:class:`InputFile`)
            Sticker file to add
        
    """

    ID: str = Field("addFavoriteSticker", alias="@type")
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> AddFavoriteSticker:
        return AddFavoriteSticker.construct(**q)
