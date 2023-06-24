# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class AnswerCustomQuery(BaseObject):
    """
    Answers a custom query; for bots only

    :param custom_query_id: Identifier of a custom query
    :type custom_query_id: :class:`Int64`
    :param data: JSON-serialized answer to the query
    :type data: :class:`String`
    """

    ID: typing.Literal["answerCustomQuery"] = "answerCustomQuery"
    custom_query_id: Int64
    data: String
