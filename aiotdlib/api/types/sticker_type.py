# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .mask_position import MaskPosition
from ..base_object import BaseObject


class StickerType(BaseObject):
    """
    Describes type of a sticker
    
    """

    ID: str = Field("stickerType", alias="@type")


class StickerTypeAnimated(StickerType):
    """
    The sticker is an animation in TGS format
    
    """

    ID: str = Field("stickerTypeAnimated", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerTypeAnimated:
        return StickerTypeAnimated.construct(**q)


class StickerTypeMask(StickerType):
    """
    The sticker is a mask in WEBP format to be placed on photos or videos
    
    :param mask_position: Position where the mask is placed; may be null, defaults to None
    :type mask_position: :class:`MaskPosition`, optional
    
    """

    ID: str = Field("stickerTypeMask", alias="@type")
    mask_position: typing.Optional[MaskPosition] = None

    @staticmethod
    def read(q: dict) -> StickerTypeMask:
        return StickerTypeMask.construct(**q)


class StickerTypeStatic(StickerType):
    """
    The sticker is an image in WEBP format
    
    """

    ID: str = Field("stickerTypeStatic", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerTypeStatic:
        return StickerTypeStatic.construct(**q)


class StickerTypeVideo(StickerType):
    """
    The sticker is a video in WEBM format
    
    """

    ID: str = Field("stickerTypeVideo", alias="@type")

    @staticmethod
    def read(q: dict) -> StickerTypeVideo:
        return StickerTypeVideo.construct(**q)
