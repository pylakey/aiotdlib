# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *

from ..types.all import (
    InlineQueryResultsButton,
    InputInlineQueryResult,
)


class AnswerInlineQuery(BaseObject):
    """
    Sets the result of an inline query; for bots only

    :param inline_query_id: Identifier of the inline query
    :type inline_query_id: :class:`Int64`
    :param results: The results of the query
    :type results: :class:`Vector[InputInlineQueryResult]`
    :param cache_time: Allowed time to cache the results of the query, in seconds
    :type cache_time: :class:`Int32`
    :param next_offset: Offset for the next inline query; pass an empty string if there are no more results
    :type next_offset: :class:`String`
    :param is_personal: Pass true if results may be cached and returned only for the user that sent the query. By default, results may be returned to any user who sends the same query
    :type is_personal: :class:`Bool`
    :param button: Button to be shown above inline query results; pass null if none, defaults to None
    :type button: :class:`InlineQueryResultsButton`, optional
    """

    ID: typing.Literal["answerInlineQuery"] = "answerInlineQuery"
    inline_query_id: Int64
    results: Vector[InputInlineQueryResult]
    cache_time: Int32
    next_offset: String
    is_personal: Bool = False
    button: typing.Optional[InlineQueryResultsButton] = None
