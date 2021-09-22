# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .labeled_price_part import LabeledPricePart
from ..base_object import BaseObject


class ShippingOption(BaseObject):
    """
    One shipping option
    
    :param id: Shipping option identifier
    :type id: :class:`str`
    
    :param title: Option title
    :type title: :class:`str`
    
    :param price_parts: A list of objects used to calculate the total shipping costs
    :type price_parts: :class:`list[LabeledPricePart]`
    
    """

    ID: str = Field("shippingOption", alias="@type")
    id: str
    title: str
    price_parts: list[LabeledPricePart]

    @staticmethod
    def read(q: dict) -> ShippingOption:
        return ShippingOption.construct(**q)
