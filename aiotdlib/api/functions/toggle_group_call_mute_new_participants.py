# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallMuteNewParticipants(BaseObject):
    """
    Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_change_mute_new_participants group call flag
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param mute_new_participants: New value of the mute_new_participants setting
    :type mute_new_participants: :class:`bool`
    
    """

    ID: str = Field("toggleGroupCallMuteNewParticipants", alias="@type")
    group_call_id: int
    mute_new_participants: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallMuteNewParticipants:
        return ToggleGroupCallMuteNewParticipants.construct(**q)
