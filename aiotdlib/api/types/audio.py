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
    
    :param duration: Duration of the audio, in seconds; as defined by the sender
    :type duration: :class:`int`
    
    :param title: Title of the audio; as defined by the sender
    :type title: :class:`str`
    
    :param performer: Performer of the audio; as defined by the sender
    :type performer: :class:`str`
    
    :param file_name: Original name of the file; as defined by the sender
    :type file_name: :class:`str`
    
    :param mime_type: The MIME type of the file; as defined by the sender
    :type mime_type: :class:`str`
    
    :param album_cover_minithumbnail: The minithumbnail of the album cover; may be null, defaults to None
    :type album_cover_minithumbnail: :class:`Minithumbnail`, optional
    
    :param album_cover_thumbnail: The thumbnail of the album cover in JPEG format; as defined by the sender. The full size thumbnail should be extracted from the downloaded file; may be null, defaults to None
    :type album_cover_thumbnail: :class:`Thumbnail`, optional
    
    :param audio: File containing the audio
    :type audio: :class:`File`
    
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
