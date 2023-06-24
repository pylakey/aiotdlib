# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    MessageSender,
)


class SetGroupCallParticipantVolumeLevel(BaseObject):
    """
    Changes volume level of a participant of an active group call. If the current user can manage the group call, then the participant's volume level will be changed for all users with the default volume level

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param participant_id: Participant identifier
    :type participant_id: :class:`MessageSender`
    :param volume_level: New participant's volume level; 1-20000 in hundreds of percents
    :type volume_level: :class:`Int32`
    """

    ID: typing.Literal["setGroupCallParticipantVolumeLevel"] = "setGroupCallParticipantVolumeLevel"
    group_call_id: Int32
    participant_id: MessageSender
    volume_level: Int32
