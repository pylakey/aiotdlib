# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    PremiumGiveawayParameters,
)


class LaunchPrepaidPremiumGiveaway(BaseObject):
    """
    Launches a prepaid Telegram Premium giveaway

    :param giveaway_id: Unique identifier of the prepaid giveaway
    :type giveaway_id: :class:`Int64`
    :param parameters: Giveaway parameters
    :type parameters: :class:`PremiumGiveawayParameters`
    """

    ID: typing.Literal["launchPrepaidPremiumGiveaway"] = Field(
        "launchPrepaidPremiumGiveaway", validation_alias="@type", alias="@type"
    )
    giveaway_id: Int64
    parameters: PremiumGiveawayParameters
