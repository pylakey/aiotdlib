# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .auto_download_settings import AutoDownloadSettings
from ..base_object import BaseObject


class AutoDownloadSettingsPresets(BaseObject):
    """
    Contains auto-download settings presets for the user
    
    Params:
        low (:class:`AutoDownloadSettings`)
            Preset with lowest settings; supposed to be used by default when roaming
        
        medium (:class:`AutoDownloadSettings`)
            Preset with medium settings; supposed to be used by default when using mobile data
        
        high (:class:`AutoDownloadSettings`)
            Preset with highest settings; supposed to be used by default when connected on Wi-Fi
        
    """

    ID: str = Field("autoDownloadSettingsPresets", alias="@type")
    low: AutoDownloadSettings
    medium: AutoDownloadSettings
    high: AutoDownloadSettings

    @staticmethod
    def read(q: dict) -> AutoDownloadSettingsPresets:
        return AutoDownloadSettingsPresets.construct(**q)
