# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputCredentials
from ..types import InputInvoice


class SendPaymentForm(BaseObject):
    """
    Sends a filled-out payment form to the bot for final verification
    
    :param input_invoice: The invoice
    :type input_invoice: :class:`InputInvoice`
    
    :param payment_form_id: Payment form identifier returned by getPaymentForm
    :type payment_form_id: :class:`int`
    
    :param order_info_id: Identifier returned by validateOrderInfo, or an empty string
    :type order_info_id: :class:`str`
    
    :param shipping_option_id: Identifier of a chosen shipping option, if applicable
    :type shipping_option_id: :class:`str`
    
    :param credentials: The credentials chosen by user for payment
    :type credentials: :class:`InputCredentials`
    
    :param tip_amount: Chosen by the user amount of tip in the smallest units of the currency
    :type tip_amount: :class:`int`
    
    """

    ID: str = Field("sendPaymentForm", alias="@type")
    input_invoice: InputInvoice
    payment_form_id: int
    order_info_id: str
    shipping_option_id: str
    credentials: InputCredentials
    tip_amount: int

    @staticmethod
    def read(q: dict) -> SendPaymentForm:
        return SendPaymentForm.construct(**q)
