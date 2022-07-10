# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputInlineQueryResult


class AnswerWebAppQuery(BaseObject):
    """
    Sets the result of interaction with a Web App and sends corresponding message on behalf of the user to the chat from which the query originated; for bots only
    
    :param web_app_query_id: Identifier of the Web App query
    :type web_app_query_id: :class:`str`
    
    :param result: The result of the query
    :type result: :class:`InputInlineQueryResult`
    
    """

    ID: str = Field("answerWebAppQuery", alias="@type")
    web_app_query_id: str
    result: InputInlineQueryResult

    @staticmethod
    def read(q: dict) -> AnswerWebAppQuery:
        return AnswerWebAppQuery.construct(**q)
