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
    
    :param callback_query_id: Identifier of the callback query
    :type callback_query_id: :class:`int`
    
    :param text: Text of the answer
    :type text: :class:`str`
    
    :param show_alert: Pass true to show an alert to the user instead of a toast notification
    :type show_alert: :class:`bool`
    
    :param url: URL to be opened
    :type url: :class:`str`
    
    :param cache_time: Time during which the result of the query can be cached, in seconds
    :type cache_time: :class:`int`
    
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
