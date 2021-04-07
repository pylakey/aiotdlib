# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .group_call_join_response_candidate import GroupCallJoinResponseCandidate
from .group_call_payload import GroupCallPayload
from ..base_object import BaseObject


class GroupCallJoinResponse(BaseObject):
    """
    Describes a group call join response
    
    """

    ID: str = Field("groupCallJoinResponse", alias="@type")


class GroupCallJoinResponseStream(GroupCallJoinResponse):
    """
    Describes that group call needs to be joined as a stream
    
    """

    ID: str = Field("groupCallJoinResponseStream", alias="@type")

    @staticmethod
    def read(q: dict) -> GroupCallJoinResponseStream:
        return GroupCallJoinResponseStream.construct(**q)


class GroupCallJoinResponseWebrtc(GroupCallJoinResponse):
    """
    Contains data needed to join the group call with WebRTC
    
    Params:
        payload (:class:`GroupCallPayload`)
            Group call payload to pass to tgcalls
        
        candidates (:obj:`list[GroupCallJoinResponseCandidate]`)
            Join response candidates to pass to tgcalls
        
    """

    ID: str = Field("groupCallJoinResponseWebrtc", alias="@type")
    payload: GroupCallPayload
    candidates: list[GroupCallJoinResponseCandidate]

    @staticmethod
    def read(q: dict) -> GroupCallJoinResponseWebrtc:
        return GroupCallJoinResponseWebrtc.construct(**q)
