# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallScreenSharingIsPaused(BaseObject):
    """
    Pauses or unpauses screen sharing in a joined group call
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param is_paused: True if screen sharing is paused
    :type is_paused: :class:`bool`
    
    """

    ID: str = Field("toggleGroupCallScreenSharingIsPaused", alias="@type")
    group_call_id: int
    is_paused: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallScreenSharingIsPaused:
        return ToggleGroupCallScreenSharingIsPaused.construct(**q)
