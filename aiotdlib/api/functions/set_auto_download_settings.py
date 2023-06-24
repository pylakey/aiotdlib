# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    AutoDownloadSettings,
    NetworkType,
)


class SetAutoDownloadSettings(BaseObject):
    """
    Sets auto-download settings

    :param settings: New user auto-download settings
    :type settings: :class:`AutoDownloadSettings`
    :param type_: Type of the network for which the new settings are relevant
    :type type_: :class:`NetworkType`
    """

    ID: typing.Literal["setAutoDownloadSettings"] = "setAutoDownloadSettings"
    settings: AutoDownloadSettings
    type_: NetworkType = Field(..., alias="type")
