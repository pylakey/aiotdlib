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


class AssignGooglePlayTransaction(BaseObject):
    """
    Informs server about a purchase through Google Play. For official applications only

    :param package_name: Application package name
    :type package_name: :class:`String`
    :param store_product_id: Identifier of the purchased store product
    :type store_product_id: :class:`String`
    :param purchase_token: Google Play purchase token
    :type purchase_token: :class:`String`
    :param purpose: Transaction purpose
    :type purpose: :class:`StorePaymentPurpose`
    """

    ID: typing.Literal["assignGooglePlayTransaction"] = "assignGooglePlayTransaction"
    package_name: String
    store_product_id: String
    purchase_token: String
    purpose: StorePaymentPurpose
