# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .shipping_option import ShippingOption
from ..base_object import BaseObject


class ValidatedOrderInfo(BaseObject):
    """
    Contains a temporary identifier of validated order information, which is stored for one hour. Also contains the available shipping options
    
    Params:
        order_info_id (:class:`str`)
            Temporary identifier of the order information
        
        shipping_options (:obj:`list[ShippingOption]`)
            Available shipping options
        
    """

    ID: str = Field("validatedOrderInfo", alias="@type")
    order_info_id: str
    shipping_options: list[ShippingOption]

    @staticmethod
    def read(q: dict) -> ValidatedOrderInfo:
        return ValidatedOrderInfo.construct(**q)
