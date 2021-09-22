# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchStickers(BaseObject):
    """
    Searches for stickers from public sticker sets that correspond to a given emoji
    
    :param emoji: String representation of emoji; must be non-empty
    :type emoji: :class:`str`
    
    :param limit: The maximum number of stickers to be returned
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchStickers", alias="@type")
    emoji: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchStickers:
        return SearchStickers.construct(**q)
