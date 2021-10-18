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
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param time_offset: Point in time when the stream segment begins; Unix timestamp in milliseconds
    :type time_offset: :class:`int`
    
    :param scale: Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
    :type scale: :class:`int`
    
    :param channel_id: Identifier of an audio/video channel to get as received from tgcalls
    :type channel_id: :class:`int`
    
    :param video_quality: Video quality as received from tgcalls; pass null to get the worst available quality
    :type video_quality: :class:`GroupCallVideoQuality`
    
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
