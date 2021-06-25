# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class JoinGroupCall(BaseObject):
    """
    Joins an active group call. Returns join response payload for tgcalls
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        participant_id (:class:`MessageSender`)
            Identifier of a group call participant, which will be used to join the call; voice chats only
        
        audio_source_id (:class:`int`)
            Caller audio channel synchronization source identifier; received from tgcalls
        
        payload (:class:`str`)
            Group call join payload; received from tgcalls
        
        is_muted (:class:`bool`)
            True, if the user's microphone is muted
        
        is_my_video_enabled (:class:`bool`)
            True, if the user's video is enabled
        
        invite_hash (:class:`str`)
            If non-empty, invite hash to be used to join the group call without being muted by administrators
        
    """

    ID: str = Field("joinGroupCall", alias="@type")
    group_call_id: int
    participant_id: MessageSender
    audio_source_id: int
    payload: str
    is_muted: bool
    is_my_video_enabled: bool
    invite_hash: str

    @staticmethod
    def read(q: dict) -> JoinGroupCall:
        return JoinGroupCall.construct(**q)
