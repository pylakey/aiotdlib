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
    
    :param duration: Duration of the animation, in seconds; as defined by the sender
    :type duration: :class:`int`
    
    :param width: Width of the animation
    :type width: :class:`int`
    
    :param height: Height of the animation
    :type height: :class:`int`
    
    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`str`
    
    :param mime_type: MIME type of the file, usually "image/gif" or "video/mp4"
    :type mime_type: :class:`str`
    
    :param has_stickers: True, if stickers were added to the animation. The list of corresponding sticker set can be received using getAttachedStickerSets
    :type has_stickers: :class:`bool`
    
    :param minithumbnail: Animation minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param thumbnail: Animation thumbnail in JPEG or MPEG4 format; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param animation: File containing the animation
    :type animation: :class:`File`
    
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
