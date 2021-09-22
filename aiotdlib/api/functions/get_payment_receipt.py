# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class GetPaymentReceipt(BaseObject):
    """
    Returns information about a successful payment
    
    :param chat_id: Chat identifier of the PaymentSuccessful message
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    """

    ID: str = Field("getPaymentReceipt", alias="@type")
    chat_id: int
    message_id: int

    @staticmethod
    def read(q: dict) -> GetPaymentReceipt:
        return GetPaymentReceipt.construct(**q)
