# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AnswerCustomQuery(BaseObject):
    """
    Answers a custom query; for bots only
    
    Params:
        custom_query_id (:class:`int`)
            Identifier of a custom query
        
        data (:class:`str`)
            JSON-serialized answer to the query
        
    """

    ID: str = Field("answerCustomQuery", alias="@type")
    custom_query_id: int
    data: str

    @staticmethod
    def read(q: dict) -> AnswerCustomQuery:
        return AnswerCustomQuery.construct(**q)
