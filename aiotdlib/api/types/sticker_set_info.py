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
    
    :param id: Identifier of the sticker set
    :type id: :class:`int`
    
    :param title: Title of the sticker set
    :type title: :class:`str`
    
    :param name: Name of the sticker set
    :type name: :class:`str`
    
    :param thumbnail: Sticker set thumbnail in WEBP or TGS format with width and height 100; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param thumbnail_outline: Sticker set thumbnail's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
    :type thumbnail_outline: :class:`list[ClosedVectorPath]`
    
    :param is_installed: True, if the sticker set has been installed by the current user
    :type is_installed: :class:`bool`
    
    :param is_archived: True, if the sticker set has been archived. A sticker set can't be installed and archived simultaneously
    :type is_archived: :class:`bool`
    
    :param is_official: True, if the sticker set is official
    :type is_official: :class:`bool`
    
    :param is_animated: True, is the stickers in the set are animated
    :type is_animated: :class:`bool`
    
    :param is_masks: True, if the stickers in the set are masks
    :type is_masks: :class:`bool`
    
    :param is_viewed: True for already viewed trending sticker sets
    :type is_viewed: :class:`bool`
    
    :param size: Total number of stickers in the set
    :type size: :class:`int`
    
    :param covers: Contains up to the first 5 stickers from the set, depending on the context. If the application needs more stickers the full set should be requested
    :type covers: :class:`list[Sticker]`
    
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
