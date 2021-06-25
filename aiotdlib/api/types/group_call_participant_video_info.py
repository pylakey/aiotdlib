# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .group_call_video_source_group import GroupCallVideoSourceGroup
from ..base_object import BaseObject


class GroupCallParticipantVideoInfo(BaseObject):
    """
    Contains information about a group call participant's video channel
    
    Params:
        source_groups (:obj:`list[GroupCallVideoSourceGroup]`)
            List of synchronization source groups of the video
        
        endpoint_id (:class:`str`)
            Video channel endpoint identifier
        
        is_paused (:class:`bool`)
            True if the video is paused. This flag needs to be ignored, if new video frames are received
        
    """

    ID: str = Field("groupCallParticipantVideoInfo", alias="@type")
    source_groups: list[GroupCallVideoSourceGroup]
    endpoint_id: str
    is_paused: bool

    @staticmethod
    def read(q: dict) -> GroupCallParticipantVideoInfo:
        return GroupCallParticipantVideoInfo.construct(**q)
