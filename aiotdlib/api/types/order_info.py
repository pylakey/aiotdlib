# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .address import Address
from ..base_object import BaseObject


class OrderInfo(BaseObject):
    """
    Order information
    
    Params:
        name (:class:`str`)
            Name of the user
        
        phone_number (:class:`str`)
            Phone number of the user
        
        email_address (:class:`str`)
            Email address of the user
        
        shipping_address (:class:`Address`)
            Shipping address for this order; may be null
        
    """

    ID: str = Field("orderInfo", alias="@type")
    name: str
    phone_number: str
    email_address: str
    shipping_address: typing.Optional[Address] = None

    @staticmethod
    def read(q: dict) -> OrderInfo:
        return OrderInfo.construct(**q)
