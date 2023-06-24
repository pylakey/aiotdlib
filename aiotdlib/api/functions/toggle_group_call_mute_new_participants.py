# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ToggleGroupCallMuteNewParticipants(BaseObject):
    """
    Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_toggle_mute_new_participants group call flag

    :param group_call_id: Group call identifier
    :type group_call_id: :class:`Int32`
    :param mute_new_participants: New value of the mute_new_participants setting
    :type mute_new_participants: :class:`Bool`
    """

    ID: typing.Literal["toggleGroupCallMuteNewParticipants"] = "toggleGroupCallMuteNewParticipants"
    group_call_id: Int32
    mute_new_participants: Bool
