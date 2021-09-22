# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class AnswerPreCheckoutQuery(BaseObject):
    """
    Sets the result of a pre-checkout query; for bots only
    
    :param pre_checkout_query_id: Identifier of the pre-checkout query
    :type pre_checkout_query_id: :class:`int`
    
    :param error_message: An error message, empty on success
    :type error_message: :class:`str`
    
    """

    ID: str = Field("answerPreCheckoutQuery", alias="@type")
    pre_checkout_query_id: int
    error_message: str

    @staticmethod
    def read(q: dict) -> AnswerPreCheckoutQuery:
        return AnswerPreCheckoutQuery.construct(**q)
