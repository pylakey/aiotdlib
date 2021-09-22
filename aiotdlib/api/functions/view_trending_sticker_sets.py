# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ViewTrendingStickerSets(BaseObject):
    """
    Informs the server that some trending sticker sets have been viewed by the user
    
    :param sticker_set_ids: Identifiers of viewed trending sticker sets
    :type sticker_set_ids: :class:`list[int]`
    
    """

    ID: str = Field("viewTrendingStickerSets", alias="@type")
    sticker_set_ids: list[int]

    @staticmethod
    def read(q: dict) -> ViewTrendingStickerSets:
        return ViewTrendingStickerSets.construct(**q)
