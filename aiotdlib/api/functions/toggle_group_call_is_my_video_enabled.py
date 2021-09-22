# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallIsMyVideoEnabled(BaseObject):
    """
    Toggles whether current user's video is enabled
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param is_my_video_enabled: Pass true if the current user's video is enabled
    :type is_my_video_enabled: :class:`bool`
    
    """

    ID: str = Field("toggleGroupCallIsMyVideoEnabled", alias="@type")
    group_call_id: int
    is_my_video_enabled: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallIsMyVideoEnabled:
        return ToggleGroupCallIsMyVideoEnabled.construct(**q)
