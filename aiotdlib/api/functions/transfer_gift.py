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
    MessageSender,
)


class TransferGift(BaseObject):
    """
    Sends an upgraded gift to another user or a channel chat

    :param received_gift_id: Identifier of the gift
    :type received_gift_id: :class:`String`
    :param new_owner_id: Identifier of the user or the channel chat that will receive the gift
    :type new_owner_id: :class:`MessageSender`
    :param star_count: The amount of Telegram Stars required to pay for the transfer
    :type star_count: :class:`Int53`
    """

    ID: typing.Literal["transferGift"] = Field("transferGift", validation_alias="@type", alias="@type")
    received_gift_id: String
    new_owner_id: MessageSender
    star_count: Int53
