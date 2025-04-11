# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPremiumGiveawayPaymentOptions(BaseObject):
    """
    Returns available options for creating of Telegram Premium giveaway or manual distribution of Telegram Premium among chat members

    :param boosted_chat_id: Identifier of the supergroup or channel chat, which will be automatically boosted by receivers of the gift codes and which is administered by the user
    :type boosted_chat_id: :class:`Int53`
    """

    ID: typing.Literal["getPremiumGiveawayPaymentOptions"] = Field(
        "getPremiumGiveawayPaymentOptions", validation_alias="@type", alias="@type"
    )
    boosted_chat_id: Int53
