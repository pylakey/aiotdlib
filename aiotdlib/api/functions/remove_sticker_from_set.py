# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import InputFile
from ..base_object import BaseObject


class RemoveStickerFromSet(BaseObject):
    """
    Removes a sticker from the set to which it belongs; for bots only. The sticker set must have been created by the bot
    
    :param sticker: Sticker
    :type sticker: :class:`InputFile`
    
    """

    ID: str = Field("removeStickerFromSet", alias="@type")
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> RemoveStickerFromSet:
        return RemoveStickerFromSet.construct(**q)
