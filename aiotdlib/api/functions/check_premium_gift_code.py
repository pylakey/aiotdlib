# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class CheckPremiumGiftCode(BaseObject):
    """
    Return information about a Telegram Premium gift code

    :param code: The code to check
    :type code: :class:`String`
    """

    ID: typing.Literal["checkPremiumGiftCode"] = Field("checkPremiumGiftCode", validation_alias="@type", alias="@type")
    code: String
