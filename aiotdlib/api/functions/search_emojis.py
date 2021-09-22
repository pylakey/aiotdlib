# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..base_object import BaseObject


class SearchEmojis(BaseObject):
    """
    Searches for emojis by keywords. Supported only if the file database is enabled
    
    :param text: Text to search for
    :type text: :class:`str`
    
    :param exact_match: True, if only emojis, which exactly match text needs to be returned
    :type exact_match: :class:`bool`
    
    :param input_language_codes: List of possible IETF language tags of the user's input language; may be empty if unknown
    :type input_language_codes: :class:`list[str]`
    
    """

    ID: str = Field("searchEmojis", alias="@type")
    text: str
    exact_match: bool
    input_language_codes: list[str]

    @staticmethod
    def read(q: dict) -> SearchEmojis:
        return SearchEmojis.construct(**q)
