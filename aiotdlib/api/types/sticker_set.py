# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .closed_vector_path import ClosedVectorPath
from .emojis import Emojis
from .sticker import Sticker
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class StickerSet(BaseObject):
    """
    Represents a sticker set
    
    Params:
        id (:class:`int`)
            Identifier of the sticker set
        
        title (:class:`str`)
            Title of the sticker set
        
        name (:class:`str`)
            Name of the sticker set
        
        thumbnail (:class:`Thumbnail`)
            Sticker set thumbnail in WEBP or TGS format with width and height 100; may be null. The file can be downloaded only before the thumbnail is changed
        
        thumbnail_outline (:obj:`list[ClosedVectorPath]`)
            Sticker set thumbnail's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
        
        is_installed (:class:`bool`)
            True, if the sticker set has been installed by the current user
        
        is_archived (:class:`bool`)
            True, if the sticker set has been archived. A sticker set can't be installed and archived simultaneously
        
        is_official (:class:`bool`)
            True, if the sticker set is official
        
        is_animated (:class:`bool`)
            True, is the stickers in the set are animated
        
        is_masks (:class:`bool`)
            True, if the stickers in the set are masks
        
        is_viewed (:class:`bool`)
            True for already viewed trending sticker sets
        
        stickers (:obj:`list[Sticker]`)
            List of stickers in this set
        
        emojis (:obj:`list[Emojis]`)
            A list of emoji corresponding to the stickers in the same order. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
        
    """

    ID: str = Field("stickerSet", alias="@type")
    id: int
    title: str
    name: str
    thumbnail: typing.Optional[Thumbnail] = None
    thumbnail_outline: list[ClosedVectorPath]
    is_installed: bool
    is_archived: bool
    is_official: bool
    is_animated: bool
    is_masks: bool
    is_viewed: bool
    stickers: list[Sticker]
    emojis: list[Emojis]

    @staticmethod
    def read(q: dict) -> StickerSet:
        return StickerSet.construct(**q)
