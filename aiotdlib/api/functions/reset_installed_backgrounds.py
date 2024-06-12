# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ResetInstalledBackgrounds(BaseObject):
    """
    Resets list of installed backgrounds to its default value
    """

    ID: typing.Literal["resetInstalledBackgrounds"] = Field(
        "resetInstalledBackgrounds", validation_alias="@type", alias="@type"
    )
