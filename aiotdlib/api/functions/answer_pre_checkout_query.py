# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AnswerPreCheckoutQuery(BaseObject):
    """
    Sets the result of a pre-checkout query; for bots only
    
    Params:
        pre_checkout_query_id (:class:`int`)
            Identifier of the pre-checkout query
        
        error_message (:class:`str`)
            An error message, empty on success
        
    """

    ID: str = Field("answerPreCheckoutQuery", alias="@type")
    pre_checkout_query_id: int
    error_message: str

    @staticmethod
    def read(q: dict) -> AnswerPreCheckoutQuery:
        return AnswerPreCheckoutQuery.construct(**q)
