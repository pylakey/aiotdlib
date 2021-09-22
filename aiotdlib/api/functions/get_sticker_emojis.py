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


class GetStickerEmojis(BaseObject):
    """
    Returns emoji corresponding to a sticker. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
    
    :param sticker: Sticker file identifier
    :type sticker: :class:`InputFile`
    
    """

    ID: str = Field("getStickerEmojis", alias="@type")
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> GetStickerEmojis:
        return GetStickerEmojis.construct(**q)
