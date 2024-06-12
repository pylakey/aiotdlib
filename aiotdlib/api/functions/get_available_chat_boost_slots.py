# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetAvailableChatBoostSlots(BaseObject):
    """
    Returns the list of available chat boost slots for the current user
    """

    ID: typing.Literal["getAvailableChatBoostSlots"] = Field(
        "getAvailableChatBoostSlots", validation_alias="@type", alias="@type"
    )
