# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types.base import *


class SearchEmojis(BaseObject):
    """
    Searches for emojis by keywords. Supported only if the file database is enabled

    :param text: Text to search for
    :type text: :class:`String`
    :param exact_match: Pass true if only emojis, which exactly match the text, needs to be returned
    :type exact_match: :class:`Bool`
    :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown
    :type input_language_codes: :class:`Vector[String]`
    """

    ID: typing.Literal["searchEmojis"] = "searchEmojis"
    text: String
    exact_match: Bool = False
    input_language_codes: Vector[String] = []
