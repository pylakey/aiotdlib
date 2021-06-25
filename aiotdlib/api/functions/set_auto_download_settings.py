# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import AutoDownloadSettings
from ..types import NetworkType


class SetAutoDownloadSettings(BaseObject):
    """
    Sets auto-download settings
    
    Params:
        settings (:class:`AutoDownloadSettings`)
            New user auto-download settings
        
        type_ (:class:`NetworkType`)
            Type of the network for which the new settings are relevant
        
    """

    ID: str = Field("setAutoDownloadSettings", alias="@type")
    settings: AutoDownloadSettings
    type_: NetworkType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> SetAutoDownloadSettings:
        return SetAutoDownloadSettings.construct(**q)
