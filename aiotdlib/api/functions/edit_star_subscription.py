# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class EditStarSubscription(BaseObject):
    """
    Cancels or re-enables Telegram Star subscription

    :param subscription_id: Identifier of the subscription to change
    :type subscription_id: :class:`String`
    :param is_canceled: New value of is_canceled
    :type is_canceled: :class:`Bool`
    """

    ID: typing.Literal["editStarSubscription"] = Field("editStarSubscription", validation_alias="@type", alias="@type")
    subscription_id: String
    is_canceled: Bool
