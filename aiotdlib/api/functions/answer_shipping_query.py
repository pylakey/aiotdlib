# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import ShippingOption
from ..base_object import BaseObject


class AnswerShippingQuery(BaseObject):
    """
    Sets the result of a shipping query; for bots only
    
    :param shipping_query_id: Identifier of the shipping query
    :type shipping_query_id: :class:`int`
    
    :param shipping_options: Available shipping options
    :type shipping_options: :class:`list[ShippingOption]`
    
    :param error_message: An error message, empty on success
    :type error_message: :class:`str`
    
    """

    ID: str = Field("answerShippingQuery", alias="@type")
    shipping_query_id: int
    shipping_options: list[ShippingOption]
    error_message: str

    @staticmethod
    def read(q: dict) -> AnswerShippingQuery:
        return AnswerShippingQuery.construct(**q)
