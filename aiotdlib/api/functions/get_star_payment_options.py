# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStarPaymentOptions(BaseObject):
    """
    Returns available options for Telegram Stars purchase
    """

    ID: typing.Literal["getStarPaymentOptions"] = Field(
        "getStarPaymentOptions", validation_alias="@type", alias="@type"
    )
