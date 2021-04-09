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


class Audio(BaseObject):
    """
    Describes an audio file. Audio is usually in MP3 or M4A format
    
    Params:
        duration (:class:`int`)
            Duration of the audio, in seconds; as defined by the sender
        
        title (:class:`str`)
            Title of the audio; as defined by the sender
        
        performer (:class:`str`)
            Performer of the audio; as defined by the sender
        
        file_name (:class:`str`)
            Original name of the file; as defined by the sender
        
        mime_type (:class:`str`)
            The MIME type of the file; as defined by the sender
        
        album_cover_minithumbnail (:class:`Minithumbnail`)
            The minithumbnail of the album cover; may be null
        
        album_cover_thumbnail (:class:`Thumbnail`)
            The thumbnail of the album cover in JPEG format; as defined by the sender. The full size thumbnail should be extracted from the downloaded file; may be null
        
        audio (:class:`File`)
            File containing the audio
        
    """

    ID: str = Field("audio", alias="@type")
    duration: int
    title: str
    performer: str
    file_name: str
    mime_type: str
    album_cover_minithumbnail: typing.Optional[Minithumbnail] = None
    album_cover_thumbnail: typing.Optional[Thumbnail] = None
    audio: File

    @staticmethod
    def read(q: dict) -> Audio:
        return Audio.construct(**q)
