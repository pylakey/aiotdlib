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
    FormattedText,
)


class SearchQuote(BaseObject):
    """
    Searches for a given quote in a text. Returns found quote start position in UTF-16 code units. Returns a 404 error if the quote is not found. Can be called synchronously

    :param text: Text in which to search for the quote
    :type text: :class:`FormattedText`
    :param quote: Quote to search for
    :type quote: :class:`FormattedText`
    :param quote_position: Approximate quote position in UTF-16 code units
    :type quote_position: :class:`Int32`
    """

    ID: typing.Literal["searchQuote"] = Field("searchQuote", validation_alias="@type", alias="@type")
    text: FormattedText
    quote: FormattedText
    quote_position: Int32
