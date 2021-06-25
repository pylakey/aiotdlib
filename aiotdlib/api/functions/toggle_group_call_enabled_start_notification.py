# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallEnabledStartNotification(BaseObject):
    """
    Toggles whether the current user will receive a notification when the group call will start; scheduled group calls only
    
    Params:
        group_call_id (:class:`int`)
            Group call identifier
        
        enabled_start_notification (:class:`bool`)
            New value of the enabled_start_notification setting
        
    """

    ID: str = Field("toggleGroupCallEnabledStartNotification", alias="@type")
    group_call_id: int
    enabled_start_notification: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallEnabledStartNotification:
        return ToggleGroupCallEnabledStartNotification.construct(**q)
