# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .auto_download_settings import AutoDownloadSettings
from ..base_object import BaseObject


class AutoDownloadSettingsPresets(BaseObject):
    """
    Contains auto-download settings presets for the current user
    
    :param low: Preset with lowest settings; supposed to be used by default when roaming
    :type low: :class:`AutoDownloadSettings`
    
    :param medium: Preset with medium settings; supposed to be used by default when using mobile data
    :type medium: :class:`AutoDownloadSettings`
    
    :param high: Preset with highest settings; supposed to be used by default when connected on Wi-Fi
    :type high: :class:`AutoDownloadSettings`
    
    """

    ID: str = Field("autoDownloadSettingsPresets", alias="@type")
    low: AutoDownloadSettings
    medium: AutoDownloadSettings
    high: AutoDownloadSettings

    @staticmethod
    def read(q: dict) -> AutoDownloadSettingsPresets:
        return AutoDownloadSettingsPresets.construct(**q)
