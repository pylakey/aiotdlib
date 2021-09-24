# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ThumbnailFormat(BaseObject):
    """
    Describes format of the thumbnail
    
    """

    ID: str = Field("thumbnailFormat", alias="@type")


class ThumbnailFormatGif(ThumbnailFormat):
    """
    The thumbnail is in static GIF format. It will be used only for some bot inline results
    
    """

    ID: str = Field("thumbnailFormatGif", alias="@type")

    @staticmethod
    def read(q: dict) -> ThumbnailFormatGif:
        return ThumbnailFormatGif.construct(**q)


class ThumbnailFormatJpeg(ThumbnailFormat):
    """
    The thumbnail is in JPEG format
    
    """

    ID: str = Field("thumbnailFormatJpeg", alias="@type")

    @staticmethod
    def read(q: dict) -> ThumbnailFormatJpeg:
        return ThumbnailFormatJpeg.construct(**q)


class ThumbnailFormatMpeg4(ThumbnailFormat):
    """
    The thumbnail is in MPEG4 format. It will be used only for some animations and videos
    
    """

    ID: str = Field("thumbnailFormatMpeg4", alias="@type")

    @staticmethod
    def read(q: dict) -> ThumbnailFormatMpeg4:
        return ThumbnailFormatMpeg4.construct(**q)


class ThumbnailFormatPng(ThumbnailFormat):
    """
    The thumbnail is in PNG format. It will be used only for background patterns
    
    """

    ID: str = Field("thumbnailFormatPng", alias="@type")

    @staticmethod
    def read(q: dict) -> ThumbnailFormatPng:
        return ThumbnailFormatPng.construct(**q)


class ThumbnailFormatTgs(ThumbnailFormat):
    """
    The thumbnail is in TGS format. It will be used only for animated sticker sets
    
    """

    ID: str = Field("thumbnailFormatTgs", alias="@type")

    @staticmethod
    def read(q: dict) -> ThumbnailFormatTgs:
        return ThumbnailFormatTgs.construct(**q)


class ThumbnailFormatWebp(ThumbnailFormat):
    """
    The thumbnail is in WEBP format. It will be used only for some stickers
    
    """

    ID: str = Field("thumbnailFormatWebp", alias="@type")

    @staticmethod
    def read(q: dict) -> ThumbnailFormatWebp:
        return ThumbnailFormatWebp.construct(**q)
