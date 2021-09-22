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


class Video(BaseObject):
    """
    Describes a video file
    
    :param duration: Duration of the video, in seconds; as defined by the sender
    :type duration: :class:`int`
    
    :param width: Video width; as defined by the sender
    :type width: :class:`int`
    
    :param height: Video height; as defined by the sender
    :type height: :class:`int`
    
    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`str`
    
    :param mime_type: MIME type of the file; as defined by the sender
    :type mime_type: :class:`str`
    
    :param has_stickers: True, if stickers were added to the video. The list of corresponding sticker sets can be received using getAttachedStickerSets
    :type has_stickers: :class:`bool`
    
    :param supports_streaming: True, if the video should be tried to be streamed
    :type supports_streaming: :class:`bool`
    
    :param minithumbnail: Video minithumbnail; may be null, defaults to None
    :type minithumbnail: :class:`Minithumbnail`, optional
    
    :param thumbnail: Video thumbnail in JPEG or MPEG4 format; as defined by the sender; may be null, defaults to None
    :type thumbnail: :class:`Thumbnail`, optional
    
    :param video: File containing the video
    :type video: :class:`File`
    
    """

    ID: str = Field("video", alias="@type")
    duration: int
    width: int
    height: int
    file_name: str
    mime_type: str
    has_stickers: bool
    supports_streaming: bool
    minithumbnail: typing.Optional[Minithumbnail] = None
    thumbnail: typing.Optional[Thumbnail] = None
    video: File

    @staticmethod
    def read(q: dict) -> Video:
        return Video.construct(**q)
