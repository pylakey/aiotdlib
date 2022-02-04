# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class TranslateText(BaseObject):
    """
    Translates a text to the given language. Returns a 404 error if the translation can't be performed
    
    :param text: Text to translate
    :type text: :class:`str`
    
    :param from_language_code: A two-letter ISO 639-1 language code of the language from which the message is translated. If empty, the language will be detected automatically
    :type from_language_code: :class:`str`
    
    :param to_language_code: A two-letter ISO 639-1 language code of the language to which the message is translated
    :type to_language_code: :class:`str`
    
    """

    ID: str = Field("translateText", alias="@type")
    text: str
    from_language_code: str
    to_language_code: str

    @staticmethod
    def read(q: dict) -> TranslateText:
        return TranslateText.construct(**q)
