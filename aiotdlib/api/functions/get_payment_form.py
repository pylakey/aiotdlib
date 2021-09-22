# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import PaymentFormTheme
from ..base_object import BaseObject


class GetPaymentForm(BaseObject):
    """
    Returns an invoice payment form. This method should be called when the user presses inlineKeyboardButtonBuy
    
    :param chat_id: Chat identifier of the Invoice message
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param theme: Preferred payment form theme
    :type theme: :class:`PaymentFormTheme`
    
    """

    ID: str = Field("getPaymentForm", alias="@type")
    chat_id: int
    message_id: int
    theme: PaymentFormTheme

    @staticmethod
    def read(q: dict) -> GetPaymentForm:
        return GetPaymentForm.construct(**q)
