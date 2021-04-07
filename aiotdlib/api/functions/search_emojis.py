# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class SearchEmojis(BaseObject):
    """
    Searches for emojis by keywords. Supported only if the file database is enabled
    
    Params:
        text (:class:`str`)
            Text to search for
        
        exact_match (:class:`bool`)
            True, if only emojis, which exactly match text needs to be returned
        
        input_language_codes (:obj:`list[str]`)
            List of possible IETF language tags of the user's input language; may be empty if unknown
        
    """

    ID: str = Field("searchEmojis", alias="@type")
    text: str
    exact_match: bool
    input_language_codes: list[str]

    @staticmethod
    def read(q: dict) -> SearchEmojis:
        return SearchEmojis.construct(**q)
