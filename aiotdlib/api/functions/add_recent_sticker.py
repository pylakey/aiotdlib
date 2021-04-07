# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class AddRecentSticker(BaseObject):
    """
    Manually adds a new sticker to the list of recently used stickers. The new sticker is added to the top of the list. If the sticker was already in the list, it is removed from the list first. Only stickers belonging to a sticker set can be added to this list
    
    Params:
        is_attached (:class:`bool`)
            Pass true to add the sticker to the list of stickers recently attached to photo or video files; pass false to add the sticker to the list of recently sent stickers
        
        sticker (:class:`InputFile`)
            Sticker file to add
        
    """

    ID: str = Field("addRecentSticker", alias="@type")
    is_attached: bool
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> AddRecentSticker:
        return AddRecentSticker.construct(**q)
