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
    BusinessOpeningHours,
)


class SetBusinessOpeningHours(BaseObject):
    """
    Changes the business opening hours of the current user. Requires Telegram Business subscription

    :param opening_hours: The new opening hours of the business; pass null to remove the opening hours; up to 28 time intervals can be specified, defaults to None
    :type opening_hours: :class:`BusinessOpeningHours`, optional
    """

    ID: typing.Literal["setBusinessOpeningHours"] = Field(
        "setBusinessOpeningHours", validation_alias="@type", alias="@type"
    )
    opening_hours: typing.Optional[BusinessOpeningHours] = None
