# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .group_call_video_source_group import GroupCallVideoSourceGroup
from ..base_object import BaseObject


class GroupCallParticipantVideoInfo(BaseObject):
    """
    Contains information about a group call participant's video channel
    
    :param source_groups: List of synchronization source groups of the video
    :type source_groups: :class:`list[GroupCallVideoSourceGroup]`
    
    :param endpoint_id: Video channel endpoint identifier
    :type endpoint_id: :class:`str`
    
    :param is_paused: True if the video is paused. This flag needs to be ignored, if new video frames are received
    :type is_paused: :class:`bool`
    
    """

    ID: str = Field("groupCallParticipantVideoInfo", alias="@type")
    source_groups: list[GroupCallVideoSourceGroup]
    endpoint_id: str
    is_paused: bool

    @staticmethod
    def read(q: dict) -> GroupCallParticipantVideoInfo:
        return GroupCallParticipantVideoInfo.construct(**q)
