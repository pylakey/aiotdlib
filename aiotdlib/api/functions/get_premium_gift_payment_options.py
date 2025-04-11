# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPremiumGiftPaymentOptions(BaseObject):
    """
    Returns available options for gifting Telegram Premium to a user
    """

    ID: typing.Literal["getPremiumGiftPaymentOptions"] = Field(
        "getPremiumGiftPaymentOptions", validation_alias="@type", alias="@type"
    )
