# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GroupCallStream(BaseObject):
    """
    Describes an available stream in a group call
    
    :param channel_id: Identifier of an audio/video channel
    :type channel_id: :class:`int`
    
    :param scale: Scale of segment durations in the stream. The duration is 1000/(2**scale) milliseconds
    :type scale: :class:`int`
    
    :param time_offset: Point in time when the stream currently ends; Unix timestamp in milliseconds
    :type time_offset: :class:`int`
    
    """

    ID: str = Field("groupCallStream", alias="@type")
    channel_id: int
    scale: int
    time_offset: int

    @staticmethod
    def read(q: dict) -> GroupCallStream:
        return GroupCallStream.construct(**q)
