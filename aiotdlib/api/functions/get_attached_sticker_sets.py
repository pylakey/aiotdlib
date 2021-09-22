# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetAttachedStickerSets(BaseObject):
    """
    Returns a list of sticker sets attached to a file. Currently only photos and videos can have attached sticker sets
    
    :param file_id: File identifier
    :type file_id: :class:`int`
    
    """

    ID: str = Field("getAttachedStickerSets", alias="@type")
    file_id: int

    @staticmethod
    def read(q: dict) -> GetAttachedStickerSets:
        return GetAttachedStickerSets.construct(**q)
