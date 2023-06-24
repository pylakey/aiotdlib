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
    InputInvoice,
    ThemeParameters,
)


class GetPaymentForm(BaseObject):
    """
    Returns an invoice payment form. This method must be called when the user presses inlineKeyboardButtonBuy

    :param input_invoice: The invoice
    :type input_invoice: :class:`InputInvoice`
    :param theme: Preferred payment form theme; pass null to use the default theme, defaults to None
    :type theme: :class:`ThemeParameters`, optional
    """

    ID: typing.Literal["getPaymentForm"] = "getPaymentForm"
    input_invoice: InputInvoice
    theme: typing.Optional[ThemeParameters] = None
