# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class PaymentResult(BaseObject):
    """
    Contains the result of a payment request
    
    :param success: True, if the payment request was successful; otherwise the verification_url will be non-empty
    :type success: :class:`bool`
    
    :param verification_url: URL for additional payment credentials verification
    :type verification_url: :class:`str`
    
    """

    ID: str = Field("paymentResult", alias="@type")
    success: bool
    verification_url: str

    @staticmethod
    def read(q: dict) -> PaymentResult:
        return PaymentResult.construct(**q)
