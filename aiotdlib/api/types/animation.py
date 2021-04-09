# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from .minithumbnail import Minithumbnail
from .thumbnail import Thumbnail
from ..base_object import BaseObject


class Animation(BaseObject):
    """
    Describes an animation file. The animation must be encoded in GIF or MPEG4 format
    
    Params:
        duration (:class:`int`)
            Duration of the animation, in seconds; as defined by the sender
        
        width (:class:`int`)
            Width of the animation
        
        height (:class:`int`)
            Height of the animation
        
        file_name (:class:`str`)
            Original name of the file; as defined by the sender
        
        mime_type (:class:`str`)
            MIME type of the file, usually "image/gif" or "video/mp4"
        
        has_stickers (:class:`bool`)
            True, if stickers were added to the animation. The list of corresponding sticker set can be received using getAttachedStickerSets
        
        minithumbnail (:class:`Minithumbnail`)
            Animation minithumbnail; may be null
        
        thumbnail (:class:`Thumbnail`)
            Animation thumbnail in JPEG or MPEG4 format; may be null
        
        animation (:class:`File`)
            File containing the animation
        
    """

    ID: str = Field("animation", alias="@type")
    duration: int
    width: int
    height: int
    file_name: str
    mime_type: str
    has_stickers: bool
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    animation: File

    @staticmethod
    def read(q: dict) -> Animation:
        return Animation.construct(**q)
