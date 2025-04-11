# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AllowUnpaidMessagesFromUser(BaseObject):
    """
    Allows the specified user to send unpaid private messages to the current user by adding a rule to userPrivacySettingAllowUnpaidMessages

    :param user_id: Identifier of the user
    :type user_id: :class:`Int53`
    :param refund_payments: Pass true to refund the user previously paid messages
    :type refund_payments: :class:`Bool`
    """

    ID: typing.Literal["allowUnpaidMessagesFromUser"] = Field(
        "allowUnpaidMessagesFromUser", validation_alias="@type", alias="@type"
    )
    user_id: Int53
    refund_payments: Bool = False
