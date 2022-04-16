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
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param participant_id: Participant identifier
    :type participant_id: :class:`MessageSender`
    
    :param is_muted: Pass true to mute the user; pass false to unmute the them
    :type is_muted: :class:`bool`
    
    """

    ID: str = Field("toggleGroupCallParticipantIsMuted", alias="@type")
    group_call_id: int
    participant_id: MessageSender
    is_muted: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallParticipantIsMuted:
        return ToggleGroupCallParticipantIsMuted.construct(**q)
