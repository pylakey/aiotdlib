# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class StartGroupCallRecording(BaseObject):
    """
    Starts recording of an active group call. Requires groupCall.can_be_managed group call flag
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        title (:class:`str`)
            Group call recording title; 0-64 characters
        
        record_video (:class:`bool`)
            Pass true to record a video file instead of an audio file
        
        use_portrait_orientation (:class:`bool`)
            Pass true to use portrait orientation for video instead of landscape one
        
    """

    ID: str = Field("startGroupCallRecording", alias="@type")
    group_call_id: int
    title: typing.Optional[str] = Field(None, max_length=64)
    record_video: bool
    use_portrait_orientation: bool

    @staticmethod
    def read(q: dict) -> StartGroupCallRecording:
        return StartGroupCallRecording.construct(**q)
