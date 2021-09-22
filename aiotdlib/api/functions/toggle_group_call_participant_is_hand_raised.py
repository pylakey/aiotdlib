# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import MessageSender
from ..base_object import BaseObject


class ToggleGroupCallParticipantIsHandRaised(BaseObject):
    """
    Toggles whether a group call participant hand is rased
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param participant_id: Participant identifier
    :type participant_id: :class:`MessageSender`
    
    :param is_hand_raised: Pass true if the user's hand should be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand
    :type is_hand_raised: :class:`bool`
    
    """

    ID: str = Field("toggleGroupCallParticipantIsHandRaised", alias="@type")
    group_call_id: int
    participant_id: MessageSender
    is_hand_raised: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallParticipantIsHandRaised:
        return ToggleGroupCallParticipantIsHandRaised.construct(**q)
