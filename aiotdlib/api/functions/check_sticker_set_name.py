# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class CheckStickerSetName(BaseObject):
    """
    Checks whether a name can be used for a new sticker set
    
    Params:
        name (:class:`str`)
            Name to be checked
        
    """

    ID: str = Field("checkStickerSetName", alias="@type")
    name: str

    @staticmethod
    def read(q: dict) -> CheckStickerSetName:
        return CheckStickerSetName.construct(**q)
