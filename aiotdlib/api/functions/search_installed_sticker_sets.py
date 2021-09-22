# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchInstalledStickerSets(BaseObject):
    """
    Searches for installed sticker sets by looking for specified query in their title and name
    
    :param is_masks: Pass true to return mask sticker sets; pass false to return ordinary sticker sets
    :type is_masks: :class:`bool`
    
    :param query: Query to search for
    :type query: :class:`str`
    
    :param limit: The maximum number of sticker sets to return
    :type limit: :class:`int`
    
    """

    ID: str = Field("searchInstalledStickerSets", alias="@type")
    is_masks: bool
    query: str
    limit: int

    @staticmethod
    def read(q: dict) -> SearchInstalledStickerSets:
        return SearchInstalledStickerSets.construct(**q)
