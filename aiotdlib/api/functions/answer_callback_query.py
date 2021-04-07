# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class AnswerCallbackQuery(BaseObject):
    """
    Sets the result of a callback query; for bots only
    
    Params:
        callback_query_id (:class:`int`)
            Identifier of the callback query
        
        text (:class:`str`)
            Text of the answer
        
        show_alert (:class:`bool`)
            If true, an alert should be shown to the user instead of a toast notification
        
        url (:class:`str`)
            URL to be opened
        
        cache_time (:class:`int`)
            Time during which the result of the query can be cached, in seconds
        
    """

    ID: str = Field("answerCallbackQuery", alias="@type")
    callback_query_id: int
    text: str
    show_alert: bool
    url: str
    cache_time: int

    @staticmethod
    def read(q: dict) -> AnswerCallbackQuery:
        return AnswerCallbackQuery.construct(**q)
