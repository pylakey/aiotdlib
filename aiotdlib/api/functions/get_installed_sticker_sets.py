# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetInstalledStickerSets(BaseObject):
    """
    Returns a list of installed sticker sets
    
    :param is_masks: Pass true to return mask sticker sets; pass false to return ordinary sticker sets
    :type is_masks: :class:`bool`
    
    """

    ID: str = Field("getInstalledStickerSets", alias="@type")
    is_masks: bool

    @staticmethod
    def read(q: dict) -> GetInstalledStickerSets:
        return GetInstalledStickerSets.construct(**q)
