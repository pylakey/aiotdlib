# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetTrendingStickerSets(BaseObject):
    """
    Returns a list of trending sticker sets. For optimal performance, the number of returned sticker sets is chosen by TDLib
    
    :param offset: The offset from which to return the sticker sets; must be non-negative
    :type offset: :class:`int`
    
    :param limit: The maximum number of sticker sets to be returned; must be non-negative. For optimal performance, the number of returned sticker sets is chosen by TDLib and can be smaller than the specified limit, even if the end of the list has not been reached
    :type limit: :class:`int`
    
    """

    ID: str = Field("getTrendingStickerSets", alias="@type")
    offset: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetTrendingStickerSets:
        return GetTrendingStickerSets.construct(**q)
