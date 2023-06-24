# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    GroupCallVideoQuality,
)


class GetGroupCallStreamSegment(BaseObject):
    """
    Returns a file with a segment of a group call stream in a modified OGG format for audio or MPEG-4 format for video

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param time_offset: Point in time when the stream segment begins; Unix timestamp in milliseconds
    :type time_offset: :class:`Int53`
    :param scale: Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
    :type scale: :class:`Int32`
    :param channel_id: Identifier of an audio/video channel to get as received from tgcalls
    :type channel_id: :class:`Int32`
    :param video_quality: Video quality as received from tgcalls; pass null to get the worst available quality, defaults to None
    :type video_quality: :class:`GroupCallVideoQuality`, optional
    """

    ID: typing.Literal["getGroupCallStreamSegment"] = "getGroupCallStreamSegment"
    group_call_id: Int32
    time_offset: Int53
    scale: Int32
    channel_id: Int32
    video_quality: typing.Optional[GroupCallVideoQuality] = None
