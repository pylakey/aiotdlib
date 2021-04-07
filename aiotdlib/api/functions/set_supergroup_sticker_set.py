# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SetSupergroupStickerSet(BaseObject):
    """
    Changes the sticker set of a supergroup; requires can_change_info administrator right
    
    Params:
        supergroup_id (:class:`int`)
            Identifier of the supergroup
        
        sticker_set_id (:class:`int`)
            New value of the supergroup sticker set identifier. Use 0 to remove the supergroup sticker set
        
    """

    ID: str = Field("setSupergroupStickerSet", alias="@type")
    supergroup_id: int
    sticker_set_id: int

    @staticmethod
    def read(q: dict) -> SetSupergroupStickerSet:
        return SetSupergroupStickerSet.construct(**q)
