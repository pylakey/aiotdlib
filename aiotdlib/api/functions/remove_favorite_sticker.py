# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class RemoveFavoriteSticker(BaseObject):
    """
    Removes a sticker from the list of favorite stickers
    
    Params:
        sticker (:class:`InputFile`)
            Sticker file to delete from the list
        
    """

    ID: str = Field("removeFavoriteSticker", alias="@type")
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> RemoveFavoriteSticker:
        return RemoveFavoriteSticker.construct(**q)
