# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetStickerSet(BaseObject):
    """
    Returns information about a sticker set by its identifier
    
    :param set_id: Identifier of the sticker set
    :type set_id: :class:`int`
    
    """

    ID: str = Field("getStickerSet", alias="@type")
    set_id: int

    @staticmethod
    def read(q: dict) -> GetStickerSet:
        return GetStickerSet.construct(**q)
