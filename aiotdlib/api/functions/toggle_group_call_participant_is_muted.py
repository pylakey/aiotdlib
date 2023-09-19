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


class ToggleGroupCallParticipantIsMuted(BaseObject):
    """
    Toggles whether a participant of an active group call is muted, unmuted, or allowed to unmute themselves

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param participant_id: Participant identifier
    :type participant_id: :class:`MessageSender`
    :param is_muted: Pass true to mute the user; pass false to unmute them
    :type is_muted: :class:`Bool`
    """

    ID: typing.Literal["toggleGroupCallParticipantIsMuted"] = "toggleGroupCallParticipantIsMuted"
    group_call_id: Int32
    participant_id: MessageSender
    is_muted: Bool = False
