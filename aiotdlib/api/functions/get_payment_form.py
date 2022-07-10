# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputInvoice
from ..types import ThemeParameters


class GetPaymentForm(BaseObject):
    """
    Returns an invoice payment form. This method must be called when the user presses inlineKeyboardButtonBuy
    
    :param input_invoice: The invoice
    :type input_invoice: :class:`InputInvoice`
    
    :param theme: Preferred payment form theme; pass null to use the default theme
    :type theme: :class:`ThemeParameters`
    
    """

    ID: str = Field("getPaymentForm", alias="@type")
    input_invoice: InputInvoice
    theme: ThemeParameters

    @staticmethod
    def read(q: dict) -> GetPaymentForm:
        return GetPaymentForm.construct(**q)
