# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import ShippingOption


class AnswerShippingQuery(BaseObject):
    """
    Sets the result of a shipping query; for bots only
    
    Params:
        shipping_query_id (:class:`int`)
            Identifier of the shipping query
        
        shipping_options (:obj:`list[ShippingOption]`)
            Available shipping options
        
        error_message (:class:`str`)
            An error message, empty on success
        
    """

    ID: str = Field("answerShippingQuery", alias="@type")
    shipping_query_id: int
    shipping_options: list[ShippingOption]
    error_message: str

    @staticmethod
    def read(q: dict) -> AnswerShippingQuery:
        return AnswerShippingQuery.construct(**q)
