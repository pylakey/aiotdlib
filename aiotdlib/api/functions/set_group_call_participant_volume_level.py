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


class SetGroupCallParticipantVolumeLevel(BaseObject):
    """
    Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with default volume level
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param participant_id: Participant identifier
    :type participant_id: :class:`MessageSender`
    
    :param volume_level: New participant's volume level; 1-20000 in hundreds of percents
    :type volume_level: :class:`int`
    
    """

    ID: str = Field("setGroupCallParticipantVolumeLevel", alias="@type")
    group_call_id: int
    participant_id: MessageSender
    volume_level: int

    @staticmethod
    def read(q: dict) -> SetGroupCallParticipantVolumeLevel:
        return SetGroupCallParticipantVolumeLevel.construct(**q)
