# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class ToggleGroupCallEnabledStartNotification(BaseObject):
    """
    Toggles whether the current user will receive a notification when the group call will start; scheduled group calls only
    
    :param group_call_id: Group call identifier
    :type group_call_id: :class:`int`
    
    :param enabled_start_notification: New value of the enabled_start_notification setting
    :type enabled_start_notification: :class:`bool`
    
    """

    ID: str = Field("toggleGroupCallEnabledStartNotification", alias="@type")
    group_call_id: int
    enabled_start_notification: bool

    @staticmethod
    def read(q: dict) -> ToggleGroupCallEnabledStartNotification:
        return ToggleGroupCallEnabledStartNotification.construct(**q)
