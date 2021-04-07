# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .file import File
from ..base_object import BaseObject


class VoiceNote(BaseObject):
    """
    Describes a voice note. The voice note must be encoded with the Opus codec, and stored inside an OGG container. Voice notes can have only a single audio channel
    
    Params:
        duration (:class:`int`)
            Duration of the voice note, in seconds; as defined by the sender
        
        waveform (:class:`str`)
            A waveform representation of the voice note in 5-bit format
        
        mime_type (:class:`str`)
            MIME type of the file; as defined by the sender
        
        voice (:class:`File`)
            File containing the voice note
        
    """

    ID: str = Field("voiceNote", alias="@type")
    duration: int
    waveform: str
    mime_type: str
    voice: File

    @staticmethod
    def read(q: dict) -> VoiceNote:
        return VoiceNote.construct(**q)
