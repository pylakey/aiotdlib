# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class GetKeywordEmojis(BaseObject):
    """
    Return emojis matching the keyword. Supported only if the file database is enabled. Order of results is unspecified

    :param text: Text to search for
    :type text: :class:`String`
    :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown
    :type input_language_codes: :class:`Vector[String]`
    """

    ID: typing.Literal["getKeywordEmojis"] = Field("getKeywordEmojis", validation_alias="@type", alias="@type")
    text: String
    input_language_codes: Vector[String] = []
