# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallScreenSharingIsPaused(BaseObject):
    """
    Pauses or unpauses screen sharing in a joined group call
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        is_paused (:class:`bool`)
            True if screen sharing is paused
        
    """

    ID: str = Field("toggleGroupCallScreenSharingIsPaused", alias="@type")
    group_call_id: int
    is_paused: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallScreenSharingIsPaused:
        return ToggleGroupCallScreenSharingIsPaused.construct(**q)
