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


class CanPurchaseFromStore(BaseObject):
    """
    Checks whether an in-store purchase is possible. Must be called before any in-store purchase

    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    """

    ID: typing.Literal["canPurchaseFromStore"] = Field("canPurchaseFromStore", validation_alias="@type", alias="@type")
    purpose: StorePaymentPurpose
