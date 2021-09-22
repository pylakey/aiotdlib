# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallIsMyVideoPaused(BaseObject):
    """
    Toggles whether current user's video is paused
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param is_my_video_paused: Pass true if the current user's video is paused
    :type is_my_video_paused: :class:`bool`
    
    """

    ID: str = Field("toggleGroupCallIsMyVideoPaused", alias="@type")
    group_call_id: int
    is_my_video_paused: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallIsMyVideoPaused:
        return ToggleGroupCallIsMyVideoPaused.construct(**q)
