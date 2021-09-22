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
    
    :param id: The payment form identifier
    :type id: :class:`int`
    
    :param invoice: Full information of the invoice
    :type invoice: :class:`Invoice`
    
    :param url: Payment form URL
    :type url: :class:`str`
    
    :param seller_bot_user_id: User identifier of the seller bot
    :type seller_bot_user_id: :class:`int`
    
    :param payments_provider_user_id: User identifier of the payment provider bot
    :type payments_provider_user_id: :class:`int`
    
    :param payments_provider: Contains information about the payment provider, if available, to support it natively without the need for opening the URL; may be null, defaults to None
    :type payments_provider: :class:`PaymentsProviderStripe`, optional
    
    :param saved_order_info: Saved server-side order information; may be null, defaults to None
    :type saved_order_info: :class:`OrderInfo`, optional
    
    :param saved_credentials: Contains information about saved card credentials; may be null, defaults to None
    :type saved_credentials: :class:`SavedCredentials`, optional
    
    :param can_save_credentials: True, if the user can choose to save credentials
    :type can_save_credentials: :class:`bool`
    
    :param need_password: True, if the user will be able to save credentials protected by a password they set up
    :type need_password: :class:`bool`
    
    """

    ID: str = Field("paymentForm", alias="@type")
    id: int
    invoice: Invoice
    url: str
    seller_bot_user_id: int
    payments_provider_user_id: int
    payments_provider: typing.Optional[PaymentsProviderStripe] = None
    saved_order_info: typing.Optional[OrderInfo] = None
    saved_credentials: typing.Optional[SavedCredentials] = None
    can_save_credentials: bool
    need_password: bool

    @staticmethod
    def read(q: dict) -> PaymentForm:
        return PaymentForm.construct(**q)
