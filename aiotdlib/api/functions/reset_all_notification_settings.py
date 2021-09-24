# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class ResetAllNotificationSettings(BaseObject):
    """
    Resets all notification settings to their default values. By default, all chats are unmuted, the sound is set to "default" and message previews are shown
    
    """

    ID: str = Field("resetAllNotificationSettings", alias="@type")

    @staticmethod
    def read(q: dict) -> ResetAllNotificationSettings:
        return ResetAllNotificationSettings.construct(**q)
