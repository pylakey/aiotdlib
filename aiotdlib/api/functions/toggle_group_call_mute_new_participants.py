# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallMuteNewParticipants(BaseObject):
    """
    Toggles whether new participants of a group call can be unmuted only by administrators of the group call. Requires groupCall.can_change_mute_new_participants group call flag
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        mute_new_participants (:class:`bool`)
            New value of the mute_new_participants setting
        
    """

    ID: str = Field("toggleGroupCallMuteNewParticipants", alias="@type")
    group_call_id: int
    mute_new_participants: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallMuteNewParticipants:
        return ToggleGroupCallMuteNewParticipants.construct(**q)
