# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetArchivedStickerSets(BaseObject):
    """
    Returns a list of archived sticker sets
    
    :param is_masks: Pass true to return mask stickers sets; pass false to return ordinary sticker sets
    :type is_masks: :class:`bool`
    
    :param offset_sticker_set_id: Identifier of the sticker set from which to return the result
    :type offset_sticker_set_id: :class:`int`
    
    :param limit: The maximum number of sticker sets to return
    :type limit: :class:`int`
    
    """

    ID: str = Field("getArchivedStickerSets", alias="@type")
    is_masks: bool
    offset_sticker_set_id: int
    limit: int

    @staticmethod
    def read(q: dict) -> GetArchivedStickerSets:
        return GetArchivedStickerSets.construct(**q)
