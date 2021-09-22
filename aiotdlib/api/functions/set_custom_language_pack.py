# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from ..types import LanguagePackInfo
from ..types import LanguagePackString
from ..base_object import BaseObject


class SetCustomLanguagePack(BaseObject):
    """
    Adds or changes a custom local language pack to the current localization target
    
    :param info: Information about the language pack. Language pack ID must start with 'X', consist only of English letters, digits and hyphens, and must not exceed 64 characters. Can be called before authorization
    :type info: :class:`LanguagePackInfo`
    
    :param strings: Strings of the new language pack
    :type strings: :class:`list[LanguagePackString]`
    
    """

    ID: str = Field("setCustomLanguagePack", alias="@type")
    info: LanguagePackInfo
    strings: list[LanguagePackString]

    @staticmethod
    def read(q: dict) -> SetCustomLanguagePack:
        return SetCustomLanguagePack.construct(**q)
