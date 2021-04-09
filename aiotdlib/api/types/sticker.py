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
    
    Params:
        set_id (:class:`int`)
            The identifier of the sticker set to which the sticker belongs; 0 if none
        
        width (:class:`int`)
            Sticker width; as defined by the sender
        
        height (:class:`int`)
            Sticker height; as defined by the sender
        
        emoji (:class:`str`)
            Emoji corresponding to the sticker
        
        is_animated (:class:`bool`)
            True, if the sticker is an animated sticker in TGS format
        
        is_mask (:class:`bool`)
            True, if the sticker is a mask
        
        mask_position (:class:`MaskPosition`)
            Position where the mask should be placed; may be null
        
        outline (:obj:`list[ClosedVectorPath]`)
            Sticker's outline represented as a list of closed vector paths; may be empty. The coordinate system origin is in the upper-left corner
        
        thumbnail (:class:`Thumbnail`)
            Sticker thumbnail in WEBP or JPEG format; may be null
        
        sticker (:class:`File`)
            File containing the sticker
        
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
