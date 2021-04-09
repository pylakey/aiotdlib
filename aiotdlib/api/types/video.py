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
    
    Params:
        duration (:class:`int`)
            Duration of the video, in seconds; as defined by the sender
        
        width (:class:`int`)
            Video width; as defined by the sender
        
        height (:class:`int`)
            Video height; as defined by the sender
        
        file_name (:class:`str`)
            Original name of the file; as defined by the sender
        
        mime_type (:class:`str`)
            MIME type of the file; as defined by the sender
        
        has_stickers (:class:`bool`)
            True, if stickers were added to the video. The list of corresponding sticker sets can be received using getAttachedStickerSets
        
        supports_streaming (:class:`bool`)
            True, if the video should be tried to be streamed
        
        minithumbnail (:class:`Minithumbnail`)
            Video minithumbnail; may be null
        
        thumbnail (:class:`Thumbnail`)
            Video thumbnail in JPEG or MPEG4 format; as defined by the sender; may be null
        
        video (:class:`File`)
            File containing the video
        
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
