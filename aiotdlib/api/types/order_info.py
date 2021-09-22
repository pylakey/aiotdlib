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
    
    :param name: Name of the user
    :type name: :class:`str`
    
    :param phone_number: Phone number of the user
    :type phone_number: :class:`str`
    
    :param email_address: Email address of the user
    :type email_address: :class:`str`
    
    :param shipping_address: Shipping address for this order; may be null, defaults to None
    :type shipping_address: :class:`Address`, optional
    
    """

    ID: str = Field("orderInfo", alias="@type")
    name: str
    phone_number: str
    email_address: str
    shipping_address: typing.Optional[Address] = None

    @staticmethod
    def read(q: dict) -> OrderInfo:
        return OrderInfo.construct(**q)
