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
    A deleted language pack string, the value should be taken from the built-in english language pack
    
    """

    ID: str = Field("languagePackStringValueDeleted", alias="@type")

    @staticmethod
    def read(q: dict) -> LanguagePackStringValueDeleted:
        return LanguagePackStringValueDeleted.construct(**q)


class LanguagePackStringValueOrdinary(LanguagePackStringValue):
    """
    An ordinary language pack string
    
    Params:
        value (:class:`str`)
            String value
        
    """

    ID: str = Field("languagePackStringValueOrdinary", alias="@type")
    value: str

    @staticmethod
    def read(q: dict) -> LanguagePackStringValueOrdinary:
        return LanguagePackStringValueOrdinary.construct(**q)


class LanguagePackStringValuePluralized(LanguagePackStringValue):
    """
    A language pack string which has different forms based on the number of some object it mentions. See https://www.unicode.org/cldr/charts/latest/supplemental/language_plural_rules.html for more info
    
    Params:
        zero_value (:class:`str`)
            Value for zero objects
        
        one_value (:class:`str`)
            Value for one object
        
        two_value (:class:`str`)
            Value for two objects
        
        few_value (:class:`str`)
            Value for few objects
        
        many_value (:class:`str`)
            Value for many objects
        
        other_value (:class:`str`)
            Default value
        
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
