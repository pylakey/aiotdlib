# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import LanguagePackInfo
from ..types import LanguagePackString


class SetCustomLanguagePack(BaseObject):
    """
    Adds or changes a custom local language pack to the current localization target
    
    Params:
        info (:class:`LanguagePackInfo`)
            Information about the language pack. Language pack ID must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization
        
        strings (:obj:`list[LanguagePackString]`)
            Strings of the new language pack
        
    """

    ID: str = Field("setCustomLanguagePack", alias="@type")
    info: LanguagePackInfo
    strings: list[LanguagePackString]

    @staticmethod
    def read(q: dict) -> SetCustomLanguagePack:
        return SetCustomLanguagePack.construct(**q)
