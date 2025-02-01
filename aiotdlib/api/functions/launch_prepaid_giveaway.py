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
    GiveawayParameters,
)


class LaunchPrepaidGiveaway(BaseObject):
    """
    Launches a prepaid giveaway

    :param giveaway_id: Unique identifier of the prepaid giveaway
    :type giveaway_id: :class:`Int64`
    :param parameters: Giveaway parameters
    :type parameters: :class:`GiveawayParameters`
    :param winner_count: The number of users to receive giveaway prize
    :type winner_count: :class:`Int32`
    :param star_count: The number of Telegram Stars to be distributed through the giveaway; pass 0 for Telegram Premium giveaways
    :type star_count: :class:`Int53`
    """

    ID: typing.Literal["launchPrepaidGiveaway"] = Field(
        "launchPrepaidGiveaway", validation_alias="@type", alias="@type"
    )
    giveaway_id: Int64
    parameters: GiveawayParameters
    winner_count: Int32
    star_count: Int53 = 0
