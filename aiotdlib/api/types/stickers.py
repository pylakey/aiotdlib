# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .sticker import Sticker
from ..base_object import BaseObject


class Stickers(BaseObject):
    """
    Represents a list of stickers
    
    Params:
        stickers (:obj:`list[Sticker]`)
            List of stickers
        
    """

    ID: str = Field("stickers", alias="@type")
    stickers: list[Sticker]

    @staticmethod
    def read(q: dict) -> Stickers:
        return Stickers.construct(**q)
