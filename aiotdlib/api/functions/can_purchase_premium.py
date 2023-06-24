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
    StorePaymentPurpose,
)


class CanPurchasePremium(BaseObject):
    """
    Checks whether Telegram Premium purchase is possible. Must be called before in-store Premium purchase

    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    """

    ID: typing.Literal["canPurchasePremium"] = "canPurchasePremium"
    purpose: StorePaymentPurpose
