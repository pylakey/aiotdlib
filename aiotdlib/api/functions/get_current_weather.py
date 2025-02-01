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
    Location,
)


class GetCurrentWeather(BaseObject):
    """
    Returns the current weather in the given location

    :param location: The location
    :type location: :class:`Location`
    """

    ID: typing.Literal["getCurrentWeather"] = Field("getCurrentWeather", validation_alias="@type", alias="@type")
    location: Location
