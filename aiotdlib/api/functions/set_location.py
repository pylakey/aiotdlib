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


class SetLocation(BaseObject):
    """
    Changes the location of the current user. Needs to be called if getOption("is_location_visible") is true and location changes for more than 1 kilometer

    :param location: The new location of the user
    :type location: :class:`Location`
    """

    ID: typing.Literal["setLocation"] = "setLocation"
    location: Location
