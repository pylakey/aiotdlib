# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InputCredentials,
    InputInvoice,
)


class SendPaymentForm(BaseObject):
    """
    Sends a filled-out payment form to the bot for final verification

    :param input_invoice: The invoice
    :type input_invoice: :class:`InputInvoice`
    :param payment_form_id: Payment form identifier returned by getPaymentForm
    :type payment_form_id: :class:`Int64`
    :param order_info_id: Identifier returned by validateOrderInfo, or an empty string
    :type order_info_id: :class:`String`
    :param shipping_option_id: Identifier of a chosen shipping option, if applicable
    :type shipping_option_id: :class:`String`
    :param tip_amount: Chosen by the user amount of tip in the smallest units of the currency
    :type tip_amount: :class:`Int53`
    :param credentials: The credentials chosen by user for payment; pass null for a payment in Telegram Stars, defaults to None
    :type credentials: :class:`InputCredentials`, optional
    """

    ID: typing.Literal["sendPaymentForm"] = Field("sendPaymentForm", validation_alias="@type", alias="@type")
    input_invoice: InputInvoice
    payment_form_id: Int64
    order_info_id: String
    shipping_option_id: String
    tip_amount: Int53
    credentials: typing.Optional[InputCredentials] = None
