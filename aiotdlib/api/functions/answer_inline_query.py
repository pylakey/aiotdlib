# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputInlineQueryResult


class AnswerInlineQuery(BaseObject):
    """
    Sets the result of an inline query; for bots only
    
    Params:
        inline_query_id (:class:`int`)
            Identifier of the inline query
        
        is_personal (:class:`bool`)
            True, if the result of the query can be cached for the specified user
        
        results (:obj:`list[InputInlineQueryResult]`)
            The results of the query
        
        cache_time (:class:`int`)
            Allowed time to cache the results of the query, in seconds
        
        next_offset (:class:`str`)
            Offset for the next inline query; pass an empty string if there are no more results
        
        switch_pm_text (:class:`str`)
            If non-empty, this text should be shown on the button that opens a private chat with the bot and sends a start message to the bot with the parameter switch_pm_parameter
        
        switch_pm_parameter (:class:`str`)
            The parameter for the bot start message
        
    """

    ID: str = Field("answerInlineQuery", alias="@type")
    inline_query_id: int
    is_personal: bool
    results: list[InputInlineQueryResult]
    cache_time: int
    next_offset: str
    switch_pm_text: str
    switch_pm_parameter: str

    @staticmethod
    def read(q: dict) -> AnswerInlineQuery:
        return AnswerInlineQuery.construct(**q)
