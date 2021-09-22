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


class RemoveFavoriteSticker(BaseObject):
    """
    Removes a sticker from the list of favorite stickers
    
    :param sticker: Sticker file to delete from the list
    :type sticker: :class:`InputFile`
    
    """

    ID: str = Field("removeFavoriteSticker", alias="@type")
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> RemoveFavoriteSticker:
        return RemoveFavoriteSticker.construct(**q)
