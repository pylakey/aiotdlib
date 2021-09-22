# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .sticker import Sticker
from ..base_object import BaseObject


class Stickers(BaseObject):
    """
    Represents a list of stickers
    
    :param stickers: List of stickers
    :type stickers: :class:`list[Sticker]`
    
    """

    ID: str = Field("stickers", alias="@type")
    stickers: list[Sticker]

    @staticmethod
    def read(q: dict) -> Stickers:
        return Stickers.construct(**q)
