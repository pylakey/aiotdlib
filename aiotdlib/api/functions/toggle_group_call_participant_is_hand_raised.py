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


class ToggleGroupCallParticipantIsHandRaised(BaseObject):
    """
    Toggles whether a group call participant hand is rased

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param participant_id: Participant identifier
    :type participant_id: :class:`MessageSender`
    :param is_hand_raised: Pass true if the user's hand needs to be raised. Only self hand can be raised. Requires groupCall.can_be_managed group call flag to lower other's hand
    :type is_hand_raised: :class:`Bool`
    """

    ID: typing.Literal["toggleGroupCallParticipantIsHandRaised"] = "toggleGroupCallParticipantIsHandRaised"
    group_call_id: Int32
    participant_id: MessageSender
    is_hand_raised: Bool = False
