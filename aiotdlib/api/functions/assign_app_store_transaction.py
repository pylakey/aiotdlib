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


class AssignAppStoreTransaction(BaseObject):
    """
    Informs server about a purchase through App Store. For official applications only

    :param receipt: App Store receipt
    :type receipt: :class:`Bytes`
    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    """

    ID: typing.Literal["assignAppStoreTransaction"] = "assignAppStoreTransaction"
    receipt: Bytes
    purpose: StorePaymentPurpose
