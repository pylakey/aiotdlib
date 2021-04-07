# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class GetEmojiSuggestionsUrl(BaseObject):
    """
    Returns an HTTP URL which can be used to automatically log in to the translation platform and suggest new emoji replacements. The URL will be valid for 30 seconds after generation
    
    Params:
        language_code (:class:`str`)
            Language code for which the emoji replacements will be suggested
        
    """

    ID: str = Field("getEmojiSuggestionsUrl", alias="@type")
    language_code: str

    @staticmethod
    def read(q: dict) -> GetEmojiSuggestionsUrl:
        return GetEmojiSuggestionsUrl.construct(**q)
