# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import OrderInfo
from ..base_object import BaseObject


class ValidateOrderInfo(BaseObject):
    """
    Validates the order information provided by a user and returns the available shipping options for a flexible invoice
    
    :param chat_id: Chat identifier of the Invoice message
    :type chat_id: :class:`int`
    
    :param message_id: Message identifier
    :type message_id: :class:`int`
    
    :param order_info: The order information, provided by the user
    :type order_info: :class:`OrderInfo`
    
    :param allow_save: True, if the order information can be saved
    :type allow_save: :class:`bool`
    
    """

    ID: str = Field("validateOrderInfo", alias="@type")
    chat_id: int
    message_id: int
    order_info: OrderInfo
    allow_save: bool

    @staticmethod
    def read(q: dict) -> ValidateOrderInfo:
        return ValidateOrderInfo.construct(**q)
