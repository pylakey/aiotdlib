# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallIsMyVideoEnabled(BaseObject):
    """
    Toggles whether current user's video is enabled
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        is_my_video_enabled (:class:`bool`)
            Pass true if the current user's video is enabled
        
    """

    ID: str = Field("toggleGroupCallIsMyVideoEnabled", alias="@type")
    group_call_id: int
    is_my_video_enabled: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallIsMyVideoEnabled:
        return ToggleGroupCallIsMyVideoEnabled.construct(**q)
