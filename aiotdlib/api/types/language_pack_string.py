# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

import typing

from pydantic import Field

from .language_pack_string_value import LanguagePackStringValue
from ..base_object import BaseObject


class LanguagePackString(BaseObject):
    """
    Represents one language pack string
    
    :param key: String key
    :type key: :class:`str`
    
    :param value: String value
    :type value: :class:`LanguagePackStringValue`
    
    """

    ID: str = Field("languagePackString", alias="@type")
    key: str
    value: LanguagePackStringValue

    @staticmethod
    def read(q: dict) -> LanguagePackString:
        return LanguagePackString.construct(**q)
