# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class UpgradeGift(BaseObject):
    """
    Upgrades a regular gift

    :param received_gift_id: Identifier of the gift
    :type received_gift_id: :class:`String`
    :param star_count: The amount of Telegram Stars required to pay for the upgrade. It the gift has prepaid_upgrade_star_count > 0, then pass 0, otherwise, pass gift.upgrade_star_count
    :type star_count: :class:`Int53`
    :param keep_original_details: Pass true to keep the original gift text, sender and receiver in the upgraded gift
    :type keep_original_details: :class:`Bool`
    """

    ID: typing.Literal["upgradeGift"] = Field("upgradeGift", validation_alias="@type", alias="@type")
    received_gift_id: String
    star_count: Int53
    keep_original_details: Bool = False
