# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetPremiumGiftCodePaymentOptions(BaseObject):
    """
    Returns available options for Telegram Premium gift code or Telegram Premium giveaway creation

    :param boosted_chat_id: Identifier of the supergroup or channel chat, which will be automatically boosted by receivers of the gift codes and which is administered by the user; 0 if none, defaults to None
    :type boosted_chat_id: :class:`Int53`, optional
    """

    ID: typing.Literal["getPremiumGiftCodePaymentOptions"] = Field(
        "getPremiumGiftCodePaymentOptions", validation_alias="@type", alias="@type"
    )
    boosted_chat_id: typing.Optional[Int53] = 0
