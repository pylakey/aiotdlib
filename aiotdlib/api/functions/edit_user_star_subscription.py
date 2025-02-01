# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EditUserStarSubscription(BaseObject):
    """
    Cancels or re-enables Telegram Star subscription for a user; for bots only

    :param user_id: User identifier
    :type user_id: :class:`Int53`
    :param telegram_payment_charge_id: Telegram payment identifier of the subscription
    :type telegram_payment_charge_id: :class:`String`
    :param is_canceled: Pass true to cancel the subscription; pass false to allow the user to enable it
    :type is_canceled: :class:`Bool`
    """

    ID: typing.Literal["editUserStarSubscription"] = Field(
        "editUserStarSubscription", validation_alias="@type", alias="@type"
    )
    user_id: Int53
    telegram_payment_charge_id: String
    is_canceled: Bool = False
