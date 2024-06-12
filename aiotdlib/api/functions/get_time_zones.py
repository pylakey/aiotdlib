# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetTimeZones(BaseObject):
    """
    Returns the list of supported time zones
    """

    ID: typing.Literal["getTimeZones"] = Field("getTimeZones", validation_alias="@type", alias="@type")
