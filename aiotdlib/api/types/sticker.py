# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .closed_vector_path import ClosedVectorPath
from .file import File
from .mask_position import MaskPosition
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class Sticker(BaseObject):
    """
    Describes a sticker
    
    :param set_id: The identifier of the sticker set to which the sticker belongs; 0 if none
    :type set_id: :class:`int`
    
    :param width: Sticker width; as defined by the sender
    :type width: :class:`int`
    
    :param height: Sticker height; as defined by the sender
    :type height: :class:`int`
    
    :param emoji: Emoji corresponding to the sticker
    :type emoji: :class:`str`
    
    :param is_animated: True, if the sticker is an animated sticker in TGS format
    :type is_animated: :class:`bool`
    
    :param is_mask: True, if the sticker is a mask
    :type is_mask: :class:`bool`
    
    :param mask_position: Position where the mask should be placed; may be null, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    
    :param outline: Sticker's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
    :type outline: :class:`list[ClosedVectorPath]`
    
    :param thumbnail: Sticker thumbnail in WEBP or JPEG format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param sticker: File containing the sticker
    :type sticker: :class:`File`
    
    """

    ID: str = Field("sticker", alias="@type")
    set_id: int
    width: int
    height: int
    emoji: str
    is_animated: bool
    is_mask: bool
    mask_position: typing.Optional[MaskPosition] = None
    outline: list[ClosedVectorPath]
    thumbnail: typing.Optional[Thumbnail] = None
    sticker: File

    @staticmethod
    def read(q: dict) -> Sticker:
        return Sticker.construct(**q)
