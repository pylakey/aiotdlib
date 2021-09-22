# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .labeled_price_part import LabeledPricePart
from ..base_object import BaseObject


class Invoice(BaseObject):
    """
    Product invoice
    
    :param currency: ISO 4217 currency code
    :type currency: :class:`str`
    
    :param price_parts: A list of objects used to calculate the total price of the product
    :type price_parts: :class:`list[LabeledPricePart]`
    
    :param max_tip_amount: The maximum allowed amount of tip in the smallest units of the currency
    :type max_tip_amount: :class:`int`
    
    :param suggested_tip_amounts: Suggested amounts of tip in the smallest units of the currency
    :type suggested_tip_amounts: :class:`list[int]`
    
    :param is_test: True, if the payment is a test payment
    :type is_test: :class:`bool`
    
    :param need_name: True, if the user's name is needed for payment
    :type need_name: :class:`bool`
    
    :param need_phone_number: True, if the user's phone number is needed for payment
    :type need_phone_number: :class:`bool`
    
    :param need_email_address: True, if the user's email address is needed for payment
    :type need_email_address: :class:`bool`
    
    :param need_shipping_address: True, if the user's shipping address is needed for payment
    :type need_shipping_address: :class:`bool`
    
    :param send_phone_number_to_provider: True, if the user's phone number will be sent to the provider
    :type send_phone_number_to_provider: :class:`bool`
    
    :param send_email_address_to_provider: True, if the user's email address will be sent to the provider
    :type send_email_address_to_provider: :class:`bool`
    
    :param is_flexible: True, if the total price depends on the shipping method
    :type is_flexible: :class:`bool`
    
    """

    ID: str = Field("invoice", alias="@type")
    currency: str
    price_parts: list[LabeledPricePart]
    max_tip_amount: int
    suggested_tip_amounts: list[int]
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
