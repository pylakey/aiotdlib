# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .closed_vector_path import ClosedVectorPath
from .sticker import Sticker
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class StickerSetInfo(BaseObject):
    """
    Represents short information about a sticker set
    
    Params:
        id (:class:`int`)
            Identifier of the sticker set
        
        title (:class:`str`)
            Title of the sticker set
        
        name (:class:`str`)
            Name of the sticker set
        
        thumbnail (:class:`Thumbnail`)
            Sticker set thumbnail in WEBP or TGS format with width and height 100; may be null
        
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
        
        size (:class:`int`)
            Total number of stickers in the set
        
        covers (:obj:`list[Sticker]`)
            Contains up to the first 5 stickers from the set, depending on the context. If the application needs more stickers the full set should be requested
        
    """

    ID: str = Field("stickerSetInfo", alias="@type")
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
    size: int
    covers: list[Sticker]

    @staticmethod
    def read(q: dict) -> StickerSetInfo:
        return StickerSetInfo.construct(**q)
