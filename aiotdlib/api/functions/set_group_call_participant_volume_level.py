# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import MessageSender


class SetGroupCallParticipantVolumeLevel(BaseObject):
    """
    Changes a group call participant's volume level. If the current user can manage the group call, then the participant's volume level will be changed for all users with default volume level
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        participant (:class:`MessageSender`)
            Participant identifier
        
        volume_level (:class:`int`)
            New participant's volume level; 1-20000 in hundreds of percents
        
    """

    ID: str = Field("setGroupCallParticipantVolumeLevel", alias="@type")
    group_call_id: int
    participant: MessageSender
    volume_level: int

    @staticmethod
    def read(q: dict) -> SetGroupCallParticipantVolumeLevel:
        return SetGroupCallParticipantVolumeLevel.construct(**q)
