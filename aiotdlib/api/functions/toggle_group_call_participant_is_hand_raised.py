# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class ToggleGroupCallParticipantIsHandRaised(BaseObject):
    """
    Toggles whether a group call participant hand is rased
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        participant (:class:`MessageSender`)
            Participant identifier
        
        is_hand_raised (:class:`bool`)
            Pass true if the user's hand should be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand
        
    """

    ID: str = Field("toggleGroupCallParticipantIsHandRaised", alias="@type")
    group_call_id: int
    participant: MessageSender
    is_hand_raised: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallParticipantIsHandRaised:
        return ToggleGroupCallParticipantIsHandRaised.construct(**q)
