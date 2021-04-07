# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetGroupCallStreamSegment(BaseObject):
    """
    Returns a file with a segment of a group call stream in a modified OGG format
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        time_offset (:class:`int`)
            Point in time when the stream segment begins; Unix timestamp in milliseconds
        
        scale (:class:`int`)
            Segment duration scale; 0-1. Segment's duration is 1000/(2**scale) milliseconds
        
    """

    ID: str = Field("getGroupCallStreamSegment", alias="@type")
    group_call_id: int
    time_offset: int
    scale: int

    @staticmethod
    def read(q: dict) -> GetGroupCallStreamSegment:
        return GetGroupCallStreamSegment.construct(**q)
