# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class RefundStarPayment(BaseObject):
    """
    Refunds a previously done payment in Telegram Stars; for bots only

    :param user_id: Identifier of the user that did the payment
    :type user_id: :class:`Int53`
    :param telegram_payment_charge_id: Telegram payment identifier
    :type telegram_payment_charge_id: :class:`String`
    """

    ID: typing.Literal["refundStarPayment"] = Field("refundStarPayment", validation_alias="@type", alias="@type")
    user_id: Int53
    telegram_payment_charge_id: String
