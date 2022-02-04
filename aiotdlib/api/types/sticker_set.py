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
from .sticker_type import StickerType
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class StickerSet(BaseObject):
    """
    Represents a sticker set
    
    :param id: Identifier of the sticker set
    :type id: :class:`int`
    
    :param title: Title of the sticker set
    :type title: :class:`str`
    
    :param name: Name of the sticker set
    :type name: :class:`str`
    
    :param thumbnail: Sticker set thumbnail in WEBP, TGS, or WEBM format with width and height 100; may be null. The file can be downloaded only before the thumbnail is changed, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param thumbnail_outline: Sticker set thumbnail's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
    :type thumbnail_outline: :class:`list[ClosedVectorPath]`
    
    :param is_installed: True, if the sticker set has been installed by the current user
    :type is_installed: :class:`bool`
    
    :param is_archived: True, if the sticker set has been archived. A sticker set can't be installed and archived simultaneously
    :type is_archived: :class:`bool`
    
    :param is_official: True, if the sticker set is official
    :type is_official: :class:`bool`
    
    :param sticker_type: Type of the stickers in the set
    :type sticker_type: :class:`StickerType`
    
    :param is_viewed: True for already viewed trending sticker sets
    :type is_viewed: :class:`bool`
    
    :param stickers: List of stickers in this set
    :type stickers: :class:`list[Sticker]`
    
    :param emojis: A list of emoji corresponding to the stickers in the same order. The list is only for informational purposes, because a sticker is always sent with a fixed emoji from the corresponding Sticker object
    :type emojis: :class:`list[Emojis]`
    
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
    sticker_type: StickerType
    is_viewed: bool
    stickers: list[Sticker]
    emojis: list[Emojis]

    @staticmethod
    def read(q: dict) -> StickerSet:
        return StickerSet.construct(**q)
