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
from .payments_provider_stripe import PaymentsProviderStripe
from .saved_credentials import SavedCredentials
from ..base_object import BaseObject


class PaymentForm(BaseObject):
    """
    Contains information about an invoice payment form
    
    Params:
        invoice (:class:`Invoice`)
            Full information of the invoice
        
        url (:class:`str`)
            Payment form URL
        
        payments_provider (:class:`PaymentsProviderStripe`)
            Contains information about the payment provider, if available, to support it natively without the need for opening the URL; may be null
        
        saved_order_info (:class:`OrderInfo`)
            Saved server-side order information; may be null
        
        saved_credentials (:class:`SavedCredentials`)
            Contains information about saved card credentials; may be null
        
        can_save_credentials (:class:`bool`)
            True, if the user can choose to save credentials
        
        need_password (:class:`bool`)
            True, if the user will be able to save credentials protected by a password they set up
        
    """

    ID: str = Field("paymentForm", alias="@type")
    invoice: Invoice
    url: str
    payments_provider: typing.Optional[PaymentsProviderStripe] = None
    saved_order_info: typing.Optional[OrderInfo] = None
    saved_credentials: typing.Optional[SavedCredentials] = None
    can_save_credentials: bool
    need_password: bool

    @staticmethod
    def read(q: dict) -> PaymentForm:
        return PaymentForm.construct(**q)
