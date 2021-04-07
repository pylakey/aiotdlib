# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ViewTrendingStickerSets(BaseObject):
    """
    Informs the server that some trending sticker sets have been viewed by the user
    
    Params:
        sticker_set_ids (:obj:`list[int]`)
            Identifiers of viewed trending sticker sets
        
    """

    ID: str = Field("viewTrendingStickerSets", alias="@type")
    sticker_set_ids: list[int]

    @staticmethod
    def read(q: dict) -> ViewTrendingStickerSets:
        return ViewTrendingStickerSets.construct(**q)
