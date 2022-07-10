# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .formatted_text import FormattedText
from .invoice import Invoice
from .order_info import OrderInfo
from .photo import Photo
from .shipping_option import ShippingOption
from ..base_object import BaseObject


class PaymentReceipt(BaseObject):
    """
    Contains information about a successful payment
    
    :param title: Product title
    :type title: :class:`str`
    
    :param param_description: Product description
    :type param_description: :class:`FormattedText`
    
    :param photo: Product photo; may be null, defaults to None
    :type photo: :class:`Photo`, optional
    
    :param date: Point in time (Unix timestamp) when the payment was made
    :type date: :class:`int`
    
    :param seller_bot_user_id: User identifier of the seller bot
    :type seller_bot_user_id: :class:`int`
    
    :param payment_provider_user_id: User identifier of the payment provider bot
    :type payment_provider_user_id: :class:`int`
    
    :param invoice: Information about the invoice
    :type invoice: :class:`Invoice`
    
    :param order_info: Order information; may be null, defaults to None
    :type order_info: :class:`OrderInfo`, optional
    
    :param shipping_option: Chosen shipping option; may be null, defaults to None
    :type shipping_option: :class:`ShippingOption`, optional
    
    :param credentials_title: Title of the saved credentials chosen by the buyer
    :type credentials_title: :class:`str`
    
    :param tip_amount: The amount of tip chosen by the buyer in the smallest units of the currency
    :type tip_amount: :class:`int`
    
    """

    ID: str = Field("paymentReceipt", alias="@type")
    title: str
    param_description: FormattedText
    photo: typing.Optional[Photo] = None
    date: int
    seller_bot_user_id: int
    payment_provider_user_id: int
    invoice: Invoice
    order_info: typing.Optional[OrderInfo] = None
    shipping_option: typing.Optional[ShippingOption] = None
    credentials_title: str
    tip_amount: int

    @staticmethod
    def read(q: dict) -> PaymentReceipt:
        return PaymentReceipt.construct(**q)
