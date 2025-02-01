# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SellGift(BaseObject):
    """
    Sells a gift for Telegram Stars

    :param received_gift_id: Identifier of the gift
    :type received_gift_id: :class:`String`
    """

    ID: typing.Literal["sellGift"] = Field("sellGift", validation_alias="@type", alias="@type")
    received_gift_id: String
