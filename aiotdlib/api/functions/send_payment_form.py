# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputCredentials


class SendPaymentForm(BaseObject):
    """
    Sends a filled-out payment form to the bot for final verification
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the Invoice message
        
        message_id (:class:`int`)
            Message identifier
        
        order_info_id (:class:`str`)
            Identifier returned by ValidateOrderInfo, or an empty string
        
        shipping_option_id (:class:`str`)
            Identifier of a chosen shipping option, if applicable
        
        credentials (:class:`InputCredentials`)
            The credentials chosen by user for payment
        
    """

    ID: str = Field("sendPaymentForm", alias="@type")
    chat_id: int
    message_id: int
    order_info_id: str
    shipping_option_id: str
    credentials: InputCredentials

    @staticmethod
    def read(q: dict) -> SendPaymentForm:
        return SendPaymentForm.construct(**q)
