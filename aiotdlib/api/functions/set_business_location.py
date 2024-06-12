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
    BusinessLocation,
)


class SetBusinessLocation(BaseObject):
    """
    Changes the business location of the current user. Requires Telegram Business subscription

    :param location: The new location of the business; pass null to remove the location, defaults to None
    :type location: :class:`BusinessLocation`, optional
    """

    ID: typing.Literal["setBusinessLocation"] = Field("setBusinessLocation", validation_alias="@type", alias="@type")
    location: typing.Optional[BusinessLocation] = None
