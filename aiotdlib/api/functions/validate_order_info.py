# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import OrderInfo


class ValidateOrderInfo(BaseObject):
    """
    Validates the order information provided by a user and returns the available shipping options for a flexible invoice
    
    Params:
        chat_id (:class:`int`)
            Chat identifier of the Invoice message
        
        message_id (:class:`int`)
            Message identifier
        
        order_info (:class:`OrderInfo`)
            The order information, provided by the user
        
        allow_save (:class:`bool`)
            True, if the order information can be saved
        
    """

    ID: str = Field("validateOrderInfo", alias="@type")
    chat_id: int
    message_id: int
    order_info: OrderInfo
    allow_save: bool

    @staticmethod
    def read(q: dict) -> ValidateOrderInfo:
        return ValidateOrderInfo.construct(**q)
