# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetPaymentReceipt(BaseObject):
    """
    Returns information about a successful payment
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the PaymentSuccessful message
        
        message_id (:class:`int`)
            Message identifier
        
    """

    ID: str = Field("getPaymentReceipt", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetPaymentReceipt:
        return GetPaymentReceipt.construct(**q)
