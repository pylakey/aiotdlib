# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetStarGiftPaymentOptions(BaseObject):
    """
    Returns available options for Telegram Stars gifting

    :param user_id: Identifier of the user that will receive Telegram Stars; pass 0 to get options for an unspecified user
    :type user_id: :class:`Int53`
    """

    ID: typing.Literal["getStarGiftPaymentOptions"] = Field(
        "getStarGiftPaymentOptions", validation_alias="@type", alias="@type"
    )
    user_id: Int53
