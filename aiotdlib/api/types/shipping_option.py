# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .labeled_price_part import LabeledPricePart
from ..base_object import BaseObject


class ShippingOption(BaseObject):
    """
    One shipping option
    
    Params:
        id (:class:`str`)
            Shipping option identifier
        
        title (:class:`str`)
            Option title
        
        price_parts (:obj:`list[LabeledPricePart]`)
            A list of objects used to calculate the total shipping costs
        
    """

    ID: str = Field("shippingOption", alias="@type")
    id: str
    title: str
    price_parts: list[LabeledPricePart]

    @staticmethod
    def read(q: dict) -> ShippingOption:
        return ShippingOption.construct(**q)
