# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputFile


class RemoveRecentSticker(BaseObject):
    """
    Removes a sticker from the list of recently used stickers
    
    Params:
        is_attached (:class:`bool`)
            Pass true to remove the sticker from the list of stickers recently attached to photo or video files; pass false to remove the sticker from the list of recently sent stickers
        
        sticker (:class:`InputFile`)
            Sticker file to delete
        
    """

    ID: str = Field("removeRecentSticker", alias="@type")
    is_attached: bool
    sticker: InputFile

    @staticmethod
    def read(q: dict) -> RemoveRecentSticker:
        return RemoveRecentSticker.construct(**q)
