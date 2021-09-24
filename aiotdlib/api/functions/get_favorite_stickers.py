# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetFavoriteStickers(BaseObject):
    """
    Returns favorite stickers
    
    """

    ID: str = Field("getFavoriteStickers", alias="@type")

    @staticmethod
    def read(q: dict) -> GetFavoriteStickers:
        return GetFavoriteStickers.construct(**q)
