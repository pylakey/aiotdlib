# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class PaymentResult(BaseObject):
    """
    Contains the result of a payment request
    
    Params:
        success (:class:`bool`)
            True, if the payment request was successful; otherwise the verification_url will be not empty
        
        verification_url (:class:`str`)
            URL for additional payment credentials verification
        
    """

    ID: str = Field("paymentResult", alias="@type")
    success: bool
    verification_url: str

    @staticmethod
    def read(q: dict) -> PaymentResult:
        return PaymentResult.construct(**q)
