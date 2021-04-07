# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetAutoDownloadSettingsPresets(BaseObject):
    """
    Returns auto-download settings presets for the current user
    
    """

    ID: str = Field("getAutoDownloadSettingsPresets", alias="@type")

    @staticmethod
    def read(q: dict) -> GetAutoDownloadSettingsPresets:
        return GetAutoDownloadSettingsPresets.construct(**q)
