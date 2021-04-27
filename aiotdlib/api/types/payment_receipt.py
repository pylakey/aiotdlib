# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .invoice import Invoice
from .order_info import OrderInfo
from .photo import Photo
from .shipping_option import ShippingOption
from ..base_object import BaseObject


class PaymentReceipt(BaseObject):
    """
    Contains information about a successful payment
    
    Params:
        title (:class:`str`)
            Product title
        
        param_description (:class:`str`)
            Product description
        
        photo (:class:`Photo`)
            Product photo; may be null
        
        date (:class:`int`)
            Point in time (Unix timestamp) when the payment was made
        
        seller_bot_user_id (:class:`int`)
            User identifier of the seller bot
        
        payments_provider_user_id (:class:`int`)
            User identifier of the payment provider bot
        
        invoice (:class:`Invoice`)
            Contains information about the invoice
        
        order_info (:class:`OrderInfo`)
            Order information; may be null
        
        shipping_option (:class:`ShippingOption`)
            Chosen shipping option; may be null
        
        credentials_title (:class:`str`)
            Title of the saved credentials chosen by the buyer
        
        tip_amount (:class:`int`)
            The amount of tip chosen by the buyer in the smallest units of the currency
        
    """

    ID: str = Field("paymentReceipt", alias="@type")
    title: str
    param_description: str
    photo: typing.Optional[Photo] = None
    date: int
    seller_bot_user_id: int
    payments_provider_user_id: int
    invoice: Invoice
    order_info: typing.Optional[OrderInfo] = None
    shipping_option: typing.Optional[ShippingOption] = None
    credentials_title: str
    tip_amount: int

    @staticmethod
    def read(q: dict) -> PaymentReceipt:
        return PaymentReceipt.construct(**q)
