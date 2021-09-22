# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ReorderInstalledStickerSets(BaseObject):
    """
    Changes the order of installed sticker sets
    
    :param is_masks: Pass true to change the order of mask sticker sets; pass false to change the order of ordinary sticker sets
    :type is_masks: :class:`bool`
    
    :param sticker_set_ids: Identifiers of installed sticker sets in the new correct order
    :type sticker_set_ids: :class:`list[int]`
    
    """

    ID: str = Field("reorderInstalledStickerSets", alias="@type")
    is_masks: bool
    sticker_set_ids: list[int]

    @staticmethod
    def read(q: dict) -> ReorderInstalledStickerSets:
        return ReorderInstalledStickerSets.construct(**q)
