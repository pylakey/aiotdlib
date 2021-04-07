# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPaymentForm(BaseObject):
    """
    Returns an invoice payment form. This method should be called when the user presses inlineKeyboardButtonBuy
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the Invoice message
        
        message_id (:class:`int`)
            Message identifier
        
    """

    ID: str = Field("getPaymentForm", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetPaymentForm:
        return GetPaymentForm.construct(**q)
