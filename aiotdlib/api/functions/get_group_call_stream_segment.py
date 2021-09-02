# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import GroupCallVideoQuality


class GetGroupCallStreamSegment(BaseObject):
    """
    Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        time_offset (:class:`int`)
            Point in time when the stream segment begins; Unix timestamp in milliseconds
        
        scale (:class:`int`)
            Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
        
        channel_id (:class:`int`)
            Identifier of an audio/video channel to get as received from tgcalls
        
        video_quality (:class:`GroupCallVideoQuality`)
            Video quality as received from tgcalls
        
    """

    ID: str = Field("getGroupCallStreamSegment", alias="@type")
    group_call_id: int
    time_offset: int
    scale: int
    channel_id: int
    video_quality: GroupCallVideoQuality

    @staticmethod
    def read(q: dict) -> GetGroupCallStreamSegment:
        return GetGroupCallStreamSegment.construct(**q)
