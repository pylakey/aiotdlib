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
from .shipping_option import ShippingOption
from ..base_object import BaseObject


class PaymentReceipt(BaseObject):
    """
    Contains information about a successful payment
    
    Params:
        date (:class:`int`)
            Point in time (Unix timestamp) when the payment was made
        
        payments_provider_user_id (:class:`int`)
            User identifier of the payment provider bot
        
        invoice (:class:`Invoice`)
            Contains information about the invoice
        
        order_info (:class:`OrderInfo`)
            Contains order information; may be null
        
        shipping_option (:class:`ShippingOption`)
            Chosen shipping option; may be null
        
        credentials_title (:class:`str`)
            Title of the saved credentials
        
    """

    ID: str = Field("paymentReceipt", alias="@type")
    date: int
    payments_provider_user_id: int
    invoice: Invoice
    order_info: typing.Optional[OrderInfo] = None
    shipping_option: typing.Optional[ShippingOption] = None
    credentials_title: str

    @staticmethod
    def read(q: dict) -> PaymentReceipt:
        return PaymentReceipt.construct(**q)
