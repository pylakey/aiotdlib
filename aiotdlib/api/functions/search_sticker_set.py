# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchStickerSet(BaseObject):
    """
    Searches for a sticker set by its name
    
    :param name: Name of the sticker set
    :type name: :class:`str`
    
    """

    ID: str = Field("searchStickerSet", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> SearchStickerSet:
        return SearchStickerSet.construct(**q)
