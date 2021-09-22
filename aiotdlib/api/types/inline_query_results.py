# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .inline_query_result import InlineQueryResult
from ..base_object import BaseObject


class InlineQueryResults(BaseObject):
    """
    Represents the results of the inline query. Use sendInlineQueryResultMessage to send the result of the query
    
    :param inline_query_id: Unique identifier of the inline query
    :type inline_query_id: :class:`int`
    
    :param next_offset: The offset for the next request. If empty, there are no more results
    :type next_offset: :class:`str`
    
    :param results: Results of the query
    :type results: :class:`list[InlineQueryResult]`
    
    :param switch_pm_text: If non-empty, this text should be shown on the button, which opens a private chat with the bot and sends the bot a start message with the switch_pm_parameter
    :type switch_pm_text: :class:`str`
    
    :param switch_pm_parameter: Parameter for the bot start message
    :type switch_pm_parameter: :class:`str`
    
    """

    ID: str = Field("inlineQueryResults", alias="@type")
    inline_query_id: int
    next_offset: str
    results: list[InlineQueryResult]
    switch_pm_text: str
    switch_pm_parameter: str

    @staticmethod
    def read(q: dict) -> InlineQueryResults:
        return InlineQueryResults.construct(**q)
