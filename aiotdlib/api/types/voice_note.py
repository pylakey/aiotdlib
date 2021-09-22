# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class VoiceNote(BaseObject):
    """
    Describes a voice note. The voice note must be encoded with the Opus codec, and stored inside an OGG container. Voice notes can have only a single audio channel
    
    :param duration: Duration of the voice note, in seconds; as defined by the sender
    :type duration: :class:`int`
    
    :param waveform: A waveform representation of the voice note in 5-bit format
    :type waveform: :class:`str`
    
    :param mime_type: MIME type of the file; as defined by the sender
    :type mime_type: :class:`str`
    
    :param voice: File containing the voice note
    :type voice: :class:`File`
    
    """

    ID: str = Field("voiceNote", alias="@type")
    duration: int
    waveform: str
    mime_type: str
    voice: File

    @staticmethod
    def read(q: dict) -> VoiceNote:
        return VoiceNote.construct(**q)
