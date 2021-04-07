# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PaymentsProviderStripe(BaseObject):
    """
    Stripe payment provider
    
    Params:
        publishable_key (:class:`str`)
            Stripe API publishable key
        
        need_country (:class:`bool`)
            True, if the user country must be provided
        
        need_postal_code (:class:`bool`)
            True, if the user ZIP/postal code must be provided
        
        need_cardholder_name (:class:`bool`)
            True, if the cardholder name must be provided
        
    """

    ID: str = Field("paymentsProviderStripe", alias="@type")
    publishable_key: str
    need_country: bool
    need_postal_code: bool
    need_cardholder_name: bool

    @staticmethod
    def read(q: dict) -> PaymentsProviderStripe:
        return PaymentsProviderStripe.construct(**q)
