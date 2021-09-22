# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SetSupergroupStickerSet(BaseObject):
    """
    Changes the sticker set of a supergroup; requires can_change_info administrator right
    
    :param supergroup_id: Identifier of the supergroup
    :type supergroup_id: :class:`int`
    
    :param sticker_set_id: New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set
    :type sticker_set_id: :class:`int`
    
    """

    ID: str = Field("setSupergroupStickerSet", alias="@type")
    supergroup_id: int
    sticker_set_id: int

    @staticmethod
    def read(q: dict) -> SetSupergroupStickerSet:
        return SetSupergroupStickerSet.construct(**q)
