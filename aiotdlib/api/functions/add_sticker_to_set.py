# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputSticker
from ..base_object import BaseObject


class AddStickerToSet(BaseObject):
    """
    Adds a new sticker to a set; for bots only. Returns the sticker set
    
    :param user_id: Sticker set owner
    :type user_id: :class:`int`
    
    :param name: Sticker set name
    :type name: :class:`str`
    
    :param sticker: Sticker to add to the set
    :type sticker: :class:`InputSticker`
    
    """

    ID: str = Field("addStickerToSet", alias="@type")
    user_id: int
    name: str
    sticker: InputSticker

    @staticmethod
    def read(q: dict) -> AddStickerToSet:
        return AddStickerToSet.construct(**q)
