# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import GroupCallPayload, MessageSender


class JoinGroupCall(BaseObject):
    """
    Joins a group call
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        participant_alias (:class:`MessageSender`)
            Identifier of the group call participant, which will be used to join the call; voice chats only
        
        payload (:class:`GroupCallPayload`)
            Group join payload; received from tgcalls
        
        source (:class:`int`)
            Caller synchronization source identifier; received from tgcalls
        
        is_muted (:class:`bool`)
            True, if the user's microphone is muted
        
        invite_hash (:class:`str`)
            If non-empty, invite hash to be used to join the group call without being muted by administrators
        
    """

    ID: str = Field("joinGroupCall", alias="@type")
    group_call_id: int
    participant_alias: MessageSender
    payload: GroupCallPayload
    source: int
    is_muted: bool
    invite_hash: str

    @staticmethod
    def read(q: dict) -> JoinGroupCall:
        return JoinGroupCall.construct(**q)
