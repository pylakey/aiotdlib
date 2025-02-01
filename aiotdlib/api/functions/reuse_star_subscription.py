# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class ReuseStarSubscription(BaseObject):
    """
    Reuses an active Telegram Star subscription to a channel chat and joins the chat again

    :param subscription_id: Identifier of the subscription
    :type subscription_id: :class:`String`
    """

    ID: typing.Literal["reuseStarSubscription"] = Field(
        "reuseStarSubscription", validation_alias="@type", alias="@type"
    )
    subscription_id: String
