# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class AnswerCustomQuery(BaseObject):
    """
    Answers a custom query; for bots only
    
    :param custom_query_id: Identifier of a custom query
    :type custom_query_id: :class:`int`
    
    :param data: JSON-serialized answer to the query
    :type data: :class:`str`
    
    """

    ID: str = Field("answerCustomQuery", alias="@type")
    custom_query_id: int
    data: str

    @staticmethod
    def read(q: dict) -> AnswerCustomQuery:
        return AnswerCustomQuery.construct(**q)
