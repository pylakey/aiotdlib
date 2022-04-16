# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject


class LanguagePackStringValue(BaseObject):
    """
    Represents the value of a string in a language pack
    
    """

    ID: str = Field("languagePackStringValue", alias="@type")


class LanguagePackStringValueDeleted(LanguagePackStringValue):
    """
    A deleted language pack string, the value must be taken from the built-in English language pack
    
    """

    ID: str = Field("languagePackStringValueDeleted", alias="@type")

    @staticmethod
    def read(q: dict) -> LanguagePackStringValueDeleted:
        return LanguagePackStringValueDeleted.construct(**q)


class LanguagePackStringValueOrdinary(LanguagePackStringValue):
    """
    An ordinary language pack string
    
    :param value: String value
    :type value: :class:`str`
    
    """

    ID: str = Field("languagePackStringValueOrdinary", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> LanguagePackStringValueOrdinary:
        return LanguagePackStringValueOrdinary.construct(**q)


class LanguagePackStringValuePluralized(LanguagePackStringValue):
    """
    A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more information
    
    :param zero_value: Value for zero objects
    :type zero_value: :class:`str`
    
    :param one_value: Value for one object
    :type one_value: :class:`str`
    
    :param two_value: Value for two objects
    :type two_value: :class:`str`
    
    :param few_value: Value for few objects
    :type few_value: :class:`str`
    
    :param many_value: Value for many objects
    :type many_value: :class:`str`
    
    :param other_value: Default value
    :type other_value: :class:`str`
    
    """

    ID: str = Field("languagePackStringValuePluralized", alias="@type")
    zero_value: str
    one_value: str
    two_value: str
    few_value: str
    many_value: str
    other_value: str

    @staticmethod
    def read(q: dict) -> LanguagePackStringValuePluralized:
        return LanguagePackStringValuePluralized.construct(**q)
