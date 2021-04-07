# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ChangeStickerSet(BaseObject):
    """
    Installs/uninstalls or activates/archives a sticker set
    
    Params:
        set_id (:class:`int`)
            Identifier of the sticker set
        
        is_installed (:class:`bool`)
            The new value of is_installed
        
        is_archived (:class:`bool`)
            The new value of is_archived. A sticker set can't be installed and archived simultaneously
        
    """

    ID: str = Field("changeStickerSet", alias="@type")
    set_id: int
    is_installed: bool
    is_archived: bool

    @staticmethod
    def read(q: dict) -> ChangeStickerSet:
        return ChangeStickerSet.construct(**q)
