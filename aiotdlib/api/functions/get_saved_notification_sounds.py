# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetSavedNotificationSounds(BaseObject):
    """
    Returns list of saved notification sounds. If a sound isn't in the list, then default sound needs to be used
    
    """

    ID: str = Field("getSavedNotificationSounds", alias="@type")

    @staticmethod
    def read(q: dict) -> GetSavedNotificationSounds:
        return GetSavedNotificationSounds.construct(**q)
