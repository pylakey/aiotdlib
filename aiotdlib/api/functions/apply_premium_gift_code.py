# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ApplyPremiumGiftCode(BaseObject):
    """
    Applies a Telegram Premium gift code

    :param code: The code to apply
    :type code: :class:`String`
    """

    ID: typing.Literal["applyPremiumGiftCode"] = Field("applyPremiumGiftCode", validation_alias="@type", alias="@type")
    code: String
