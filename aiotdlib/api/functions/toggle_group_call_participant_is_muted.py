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
    Toggles whether a group call participant is muted, unmuted, or allowed to unmute themself
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        participant (:class:`MessageSender`)
            Participant identifier
        
        is_muted (:class:`bool`)
            Pass true if the user must be muted and false otherwise
        
    """

    ID: str = Field("toggleGroupCallParticipantIsMuted", alias="@type")
    group_call_id: int
    participant: MessageSender
    is_muted: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallParticipantIsMuted:
        return ToggleGroupCallParticipantIsMuted.construct(**q)
