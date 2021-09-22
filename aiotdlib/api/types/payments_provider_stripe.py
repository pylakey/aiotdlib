# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class PaymentsProviderStripe(BaseObject):
    """
    Stripe payment provider
    
    :param publishable_key: Stripe API publishable key
    :type publishable_key: :class:`str`
    
    :param need_country: True, if the user country must be provided
    :type need_country: :class:`bool`
    
    :param need_postal_code: True, if the user ZIP/postal code must be provided
    :type need_postal_code: :class:`bool`
    
    :param need_cardholder_name: True, if the cardholder name must be provided
    :type need_cardholder_name: :class:`bool`
    
    """

    ID: str = Field("paymentsProviderStripe", alias="@type")
    publishable_key: str
    need_country: bool
    need_postal_code: bool
    need_cardholder_name: bool

    @staticmethod
    def read(q: dict) -> PaymentsProviderStripe:
        return PaymentsProviderStripe.construct(**q)
