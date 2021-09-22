# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetStickers(BaseObject):
    """
    Returns stickers from the installed sticker sets that correspond to a given emoji. If the emoji is not empty, favorite and recently used stickers may also be returned
    
    :param emoji: String representation of emoji. If empty, returns all known installed stickers
    :type emoji: :class:`str`
    
    :param limit: The maximum number of stickers to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("getStickers", alias="@type")
    emoji: str
    limit: int

    @staticmethod
    def read(q: dict) -> GetStickers:
        return GetStickers.construct(**q)
