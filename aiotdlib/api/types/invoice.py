# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .labeled_price_part import LabeledPricePart
from ..base_object import BaseObject


class Invoice(BaseObject):
    """
    Product invoice
    
    Params:
        currency (:class:`str`)
            ISO 4217 currency code
        
        price_parts (:obj:`list[LabeledPricePart]`)
            A list of objects used to calculate the total price of the product
        
        is_test (:class:`bool`)
            True, if the payment is a test payment
        
        need_name (:class:`bool`)
            True, if the user's name is needed for payment
        
        need_phone_number (:class:`bool`)
            True, if the user's phone number is needed for payment
        
        need_email_address (:class:`bool`)
            True, if the user's email address is needed for payment
        
        need_shipping_address (:class:`bool`)
            True, if the user's shipping address is needed for payment
        
        send_phone_number_to_provider (:class:`bool`)
            True, if the user's phone number will be sent to the provider
        
        send_email_address_to_provider (:class:`bool`)
            True, if the user's email address will be sent to the provider
        
        is_flexible (:class:`bool`)
            True, if the total price depends on the shipping method
        
    """

    ID: str = Field("invoice", alias="@type")
    currency: str
    price_parts: list[LabeledPricePart]
    is_test: bool
    need_name: bool
    need_phone_number: bool
    need_email_address: bool
    need_shipping_address: bool
    send_phone_number_to_provider: bool
    send_email_address_to_provider: bool
    is_flexible: bool

    @staticmethod
    def read(q: dict) -> Invoice:
        return Invoice.construct(**q)
