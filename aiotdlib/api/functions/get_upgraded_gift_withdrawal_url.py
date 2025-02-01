# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetUpgradedGiftWithdrawalUrl(BaseObject):
    """
    Returns a URL for upgraded gift withdrawal in the TON blockchain as an NFT; requires owner privileges for gifts owned by a chat

    :param received_gift_id: Identifier of the gift
    :type received_gift_id: :class:`String`
    :param password: The 2-step verification password of the current user
    :type password: :class:`String`
    """

    ID: typing.Literal["getUpgradedGiftWithdrawalUrl"] = Field(
        "getUpgradedGiftWithdrawalUrl", validation_alias="@type", alias="@type"
    )
    received_gift_id: String
    password: String
