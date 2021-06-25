# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class ToggleGroupCallParticipantIsMuted(BaseObject):
    """
    Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        participant_id (:class:`MessageSender`)
            Participant identifier
        
        is_muted (:class:`bool`)
            Pass true if the user must be muted and false otherwise
        
    """

    ID: str = Field("toggleGroupCallParticipantIsMuted", alias="@type")
    group_call_id: int
    participant_id: MessageSender
    is_muted: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallParticipantIsMuted:
        return ToggleGroupCallParticipantIsMuted.construct(**q)
