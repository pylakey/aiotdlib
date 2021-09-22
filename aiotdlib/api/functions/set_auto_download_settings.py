# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import AutoDownloadSettings
from ..types import NetworkType
from ..base_object import BaseObject


class SetAutoDownloadSettings(BaseObject):
    """
    Sets auto-download settings
    
    :param settings: New user auto-download settings
    :type settings: :class:`AutoDownloadSettings`
    
    :param type_: Type of the network for which the new settings are relevant
    :type type_: :class:`NetworkType`
    
    """

    ID: str = Field("setAutoDownloadSettings", alias="@type")
    settings: AutoDownloadSettings
    type_: NetworkType = Field(..., alias='type')

    @staticmethod
    def read(q: dict) -> SetAutoDownloadSettings:
        return SetAutoDownloadSettings.construct(**q)
