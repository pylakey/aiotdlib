# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LabeledPricePart(BaseObject):
    """
    Portion of the price of a product (e.g., "delivery cost", "tax amount")
    
    Params:
        label (:class:`str`)
            Label for this portion of the product price
        
        amount (:class:`int`)
            Currency amount in minimal quantity of the currency
        
    """

    ID: str = Field("labeledPricePart", alias="@type")
    label: str
    amount: int

    @staticmethod
    def read(q: dict) -> LabeledPricePart:
        return LabeledPricePart.construct(**q)
