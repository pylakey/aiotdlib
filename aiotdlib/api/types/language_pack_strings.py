# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from .language_pack_string import LanguagePackString
from ..base_object import BaseObject


class LanguagePackStrings(BaseObject):
    """
    Contains a list of language pack strings
    
    Params:
        strings (:obj:`list[LanguagePackString]`)
            A list of language pack strings
        
    """

    ID: str = Field("languagePackStrings", alias="@type")
    strings: list[LanguagePackString]

    @staticmethod
    def read(q: dict) -> LanguagePackStrings:
        return LanguagePackStrings.construct(**q)
